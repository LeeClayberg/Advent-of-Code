
# Read in stuff
with open("files/day18.txt", "r") as file_stream:
    # Setup
    lines = file_stream.read().split('\n')[:-1]
    corrupted = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines]

    start = (0, 0)
    end = (70, 70)

    previous_path = None
    for limit in range(1024, len(corrupted)):
        corrupted_up_to = corrupted[:limit]
        if previous_path is not None and corrupted_up_to[-1] not in previous_path:
            continue
        weights = {start: 0}
        queue = [start]
        visited = set()
        while len(queue) > 0:
            x, y = queue.pop(0)
            if (x, y) == end:
                break
            if (x, y) in visited:
                continue
            visited.add((x, y))
            w = weights[(x, y)]
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx, ny = x+dx, y+dy
                if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in corrupted_up_to:
                    nw = w + 1
                    if (nx, ny) not in weights or nw < weights[(nx, ny)]:
                        weights[(nx, ny)] = nw
                        queue.append((nx, ny))
        if end not in weights:
            x, y = corrupted[limit-1]
            print(f"{x},{y}")
            break
        else:
            # Find path
            path = [end]
            while path[-1] != start:
                x, y = path[-1]
                neighbors = [(x+dx, y+dy) for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]]
                point = min(neighbors, key=lambda p: weights[p] if p in weights else 1000000000)
                path.append(point)
            previous_path = path




