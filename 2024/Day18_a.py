
# Read in stuff
with open("files/day18.txt", "r") as file_stream:
    # Setup
    lines = file_stream.read().split('\n')[:-1]
    corrupted = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in lines][:1024]

    start = (0, 0)
    end = (70, 70)

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
            if 0 <= nx < 71 and 0 <= ny < 71 and (nx, ny) not in corrupted:
                nw = w + 1
                if (nx, ny) not in weights or nw < weights[(nx, ny)]:
                    weights[(nx, ny)] = nw
                    queue.append((nx, ny))

    # grid_str = ""
    # for y in range(0, 71):
    #     row_str = ""
    #     for x in range(0, 71):
    #         if (x, y) in corrupted:
    #             row_str += "#"
    #         else:
    #             row_str += "."
    #     grid_str += row_str + '\n'
    # print(grid_str)
    # print()

    print(weights[end])




