
# Read in stuff
with open("files/day20.txt", "r") as file_stream:
    # Setup
    grid = file_stream.read().split('\n')

    # Create graph
    start = None
    graph = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                continue
            if cell == 'S':
                start = (x, y)
            neighbors = []
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx, ny = x+dx, y+dy
                if grid[ny][nx] != '#':
                    neighbors.append((nx, ny))
            graph[(x, y)] = neighbors

    # Find picoseconds
    picoseconds = {}
    point = start
    while point not in picoseconds:
        picoseconds[point] = len(picoseconds)
        for neighbor in graph[point]:
            if neighbor not in picoseconds:
                point = neighbor

    # Find cheats over 100
    cheats_over_100 = 0
    for point in picoseconds.keys():
        p = picoseconds[point]
        x, y = point
        for dx in range(-20, 21):
            for dy in range(-20, 21):
                cheat_cost = abs(dx) + abs(dy)
                if cheat_cost > 20:
                    continue
                nx, ny = x+dx, y+dy
                if (nx, ny) not in picoseconds:
                    continue
                np = picoseconds[(nx, ny)]
                if np < p:
                    continue
                cheat = np - p - cheat_cost
                if cheat >= 100:
                    cheats_over_100 += 1

    print(cheats_over_100)


