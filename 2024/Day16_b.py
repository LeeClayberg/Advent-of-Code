
# Read in stuff
with open("files/day16.txt", "r") as file_stream:
    # Setup
    grid = file_stream.read().split('\n')
    start, end = None, None
    graph = {}
    safe = {'.', 'S', 'E'}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in safe:
                for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] in safe:
                        if (x, y) not in graph:
                            graph[(x, y)] = set()
                        graph[(x, y)].add((nx, ny))
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
