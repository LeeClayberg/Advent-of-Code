
with open("files/day21.txt", "r") as file_stream:
    grid = file_stream.readlines()
    grid = [line[:-1] for line in grid]

start = None
obstacles = set()
all_cells = set()
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '.':
            continue
        elif cell == 'S':
            start = (x, y)
        elif cell == '#':
            obstacles.add((x, y))
        all_cells.add((x, y))

reachable = all_cells.difference(obstacles)



group = {start: 0}
for i in range(0, 6):
    new_group = group.copy()
    for x, y in group:
        for d_x, d_y in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            neighbor = (x+d_x, y+d_y)
            fixed_neighbor = (neighbor[0] % len(grid[0]), neighbor[1] % len(grid))
            if fixed_neighbor in obstacles:
                continue
            if fixed_neighbor not in group:
                new_group[fixed_neighbor] = 0
            new_group[fixed_neighbor] += 1
    group = new_group
print(sum(group.values()))