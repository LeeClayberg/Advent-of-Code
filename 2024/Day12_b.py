
# Read in stuff
with open("files/day12.txt", "r") as file_stream:
    lines = file_stream.readlines()
    farm = [[c for c in line[:-1]] for line in lines]

    # Calculate regions
    regions = []
    seen = set()
    for y, row in enumerate(farm):
        for x, plot in enumerate(row):
            position = (x, y)
            if position in seen:
                continue
            region = set()
            queue = [position]
            while len(queue) > 0:
                cx, cy = queue.pop(0)
                if (cx, cy) in region:
                    continue
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < len(farm[0]) and 0 <= ny < len(farm) and farm[ny][nx] == plot:
                        queue.append((nx, ny))
                region.add((cx, cy))
                seen.add((cx, cy))
            regions.append(region)

    # Find fencing
    total = 0
    for region in regions:
        # Find edge points
        edge_points = set()
        for x, y in region:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(farm[0]) and 0 <= ny < len(farm) and farm[ny][nx] == farm[y][x]):
                    cx, cy = (x+(dx*0.5), y+(dy*0.5))
                    p0 = (cx, cy)
                    edge_points.add(p0)
                    if dx == 0:
                        p1, p2 = (cx - 0.5, cy), (cx + 0.5, cy)
                        edge_points.add(p1)
                        edge_points.add(p2)
                    else:
                        p1, p2 = (cx, cy - 0.5), (cx, cy + 0.5)
                        edge_points.add(p1)
                        edge_points.add(p2)

        edge_points = sorted(edge_points, key=(lambda p: p[0] + p[1]))

        sides = 0
        seen = set()
        for edge_point in edge_points:
            if edge_point in seen:
                continue
            point = edge_point
            start = point
            direction = None
            while direction is None or point != start:
                directions = [(0, 0.5), (-0.5, 0), (0, -0.5), (0.5, 0)]
                if direction is not None:
                    idx = (directions.index((-direction[0], -direction[1])) + 1) % 4
                    directions = directions[idx:] + directions[:idx]
                for dx, dy in directions:
                    new_point = (point[0] + dx, point[1] + dy)
                    if new_point not in edge_points:
                        continue
                    if (dx, dy) != direction:
                        sides += 1
                    point = new_point
                    seen.add(new_point)
                    direction = (dx, dy)
                    break
            seen.add(point)
        total += sides * len(region)
    print(total)



