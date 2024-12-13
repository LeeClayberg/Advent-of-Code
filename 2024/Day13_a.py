
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
        perimeter = 0
        for x, y in region:
            sides = 4
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(farm[0]) and 0 <= ny < len(farm) and farm[ny][nx] == farm[y][x]:
                    sides -= 1
            perimeter += sides
        total += perimeter * len(region)
    print(total)