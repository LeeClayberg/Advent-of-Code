
walls = set()
xbounds = [10000, -1]
ybounds = [10000, -1]
with open("files/input_14.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        endpoints = line[:-1].split(" -> ")
        for i in range(len(endpoints)-1):
            x, y = [int(e) for e in endpoints[i].split(',')]
            a, b = [int(e) for e in endpoints[i+1].split(',')]
            xbounds[0] = min([xbounds[0], x, a])
            xbounds[1] = max([xbounds[1], x, a])
            ybounds[0] = min([ybounds[0], y, b])
            ybounds[1] = max([ybounds[1], y, b])

            if x == a:
                for c in range(min(y, b), max(y, b)+1):
                    walls.add((x, c))
            else:
                for c in range(min(x, a), max(x, a)+1):
                    walls.add((c, y))

ybounds[0] = min(ybounds[0], 0)
ybounds[1] = max(ybounds[1], 0) + 2
xbounds[0] = min([xbounds[0], 500, 500 - ybounds[1]])
xbounds[1] = max([xbounds[1], 500, 500 + ybounds[1]])

grid = [['#' if (m, n) in walls else '.' for m in range(xbounds[0], xbounds[1]+1)] for n in range(ybounds[0], ybounds[1]+1)]

grid_x_offset = xbounds[0]
grid_y_offset = ybounds[0]

# Fill with sand
y = 0
while y < ybounds[1]:
    for x in range(500 - y, 500 + y + 1):
        if grid[y-grid_y_offset][x-grid_x_offset] == '.':
            grid[y-grid_y_offset][x-grid_x_offset] = 'o'
    y += 1

# Remove specific sand
for i in range(len(grid)):
    for f in range(len(grid[i]) - 2):
        if ''.join(grid[i][f:f+3]) == '###' and i < len(grid) - 1:
            grid[i + 1][f + 1] = '#'

print(len([o for row in grid for o in row if o == 'o']))
