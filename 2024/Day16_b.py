
# Read in stuff
with open("files/day16.txt", "r") as file_stream:
    # Setup
    grid = [list(row) for row in file_stream.read().split('\n')]
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
                info[(x, y)] = {}
            if cell == 'S':
                start = (x, y)
                info[(x, y)] = {
                    (0, -1): (1000, set()),
                    (-1, 0): (2000, set()),
                    (1, 0): (0, set()),
                    (0, 1): (1000, set())
                }
            elif cell == 'E':
                end = (x, y)

    # Weighted the maze
    queue = [start]
    while len(queue) > 0:
        x, y = queue.pop(0)
        for dx, dy in maze[(x, y)]:
            nx, ny = x + dx, y + dy
            nw = info[(x, y)][(dx, dy)][0] + 1
            for ndx, ndy in maze[(nx, ny)]:
                nnw = nw
                if (ndx, ndy) != (dx, dy):
                    nnw += 1000

                ncw, ncf = 1000000000000, set()
                if (ndx, ndy) in info[(nx, ny)]:
                    ncw, ncf = info[(nx, ny)][(ndx, ndy)]

                if nnw <= ncw:
                    if nnw < ncw:
                        ncf = set()
                        queue.append((nx, ny))
                    ncf.add((x, y))
                    info[(nx, ny)][(ndx, ndy)] = (nnw, ncf)

    print(info[end])

    # Backtrack
    queue2 = [end]
    visited = set()
    while len(queue2) > 0:
        x, y = queue2.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if (x, y) == start:
            continue

        mw, points = None, None
        for dx, dy in info[(x, y)].keys():
            w, p = info[(x, y)][(dx, dy)]
            nx, ny = x + dx, y + dy
            if mw is None or w < mw:
                mw = w
                points = p
            if w == mw:
                points.update(p)
        queue2 += points

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) in visited:
                grid[y][x] = 'O'
    print('\n'.join([''.join(row) for row in grid]))

    print(len(visited))


