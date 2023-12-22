
with open("files/day21.txt", "r") as file_stream:
    grid = file_stream.readlines()
    grid = [line[:-1] for line in grid]

start = None
obstacles = set()
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '.':
            continue
        elif cell == 'S':
            start = (x, y)
        elif cell == '#':
            obstacles.add((x, y))


group = [start]
for i in range(0, 64):
    new_group = set()
    for x, y in group:
        for d_x, d_y in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            neighbor = (x+d_x, y+d_y)
            if 0 > neighbor[0] or neighbor[0] >= len(grid[0]) or 0 > neighbor[1] or neighbor[1] >= len(grid):
                continue
            if neighbor in obstacles:
                continue
            new_group.add(neighbor)
    group = list(new_group)
print(len(group))