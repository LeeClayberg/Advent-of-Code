
# Read in stuff
with open("files/day16.txt", "r") as file_stream:
    # Setup
    grid = file_stream.read().split('\n')
    start, end = None, None
    maze = {}
    info = {}
    safe = {'.', 'S', 'E'}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in safe:
                directions = []
                for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] in safe:
                        directions.append((dx, dy))
                maze[(x, y)] = directions
                info[(x, y)] = (None, 100000000000)
            if cell == 'S':
                start = (x, y)
                info[(x, y)] = ((1, 0), 0)
            elif cell == 'E':
                end = (x, y)

    # Weighted the maze
    queue = [start]
    while len(queue) > 0:
        x, y = queue.pop(0)
        d, w = info[(x, y)]
        for dx, dy in maze[(x, y)]:
            nx, ny = x + dx, y + dy
            nw = w + 1
            if (dx, dy) != d:
                nw += 1000
            # Update?
            cd, cw = info[(nx, ny)]
            if nw < cw:
                info[(nx, ny)] = ((dx, dy), nw)
                queue.append((nx, ny))

    print(info[end][1])



