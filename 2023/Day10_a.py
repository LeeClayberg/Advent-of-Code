
with open("files/day10.txt", "r") as file_stream:
    lines = file_stream.readlines()

dir_options = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)],
    'S': [(-1, 0), (0, -1), (0, 1), (1, 0)],
}
dir_values = {
    (-1, 0): {'|', '7', 'F'},
    (0, -1): {'-', 'L', 'F'},
    (0, 1): {'-', 'J', '7'},
    (1, 0): {'|', 'J', 'L'},
}

grid = lines
start = None
for a, row in enumerate(grid):
    for b, cell in enumerate(row):
        if cell == 'S':
            start = (a, b, 0)

queue = [start]
saved = {}
while len(queue) > 0:
    a, b, dist = queue.pop(0)
    if (a, b) in saved:
        continue

    saved[(a, b)] = dist

    value = grid[a][b]
    for c, d in dir_options[value]:
        e, f = a+c, b+d
        pos_value = grid[e][f]
        if pos_value in dir_values[(c, d)]:
            queue.append((e, f, dist+1))

print(max(saved.values()))