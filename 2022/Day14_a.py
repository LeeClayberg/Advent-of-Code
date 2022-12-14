
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

xbounds[0] = min(xbounds[0], 500)
xbounds[1] = max(xbounds[1], 500)
ybounds[0] = min(ybounds[0], 0)
ybounds[1] = max(ybounds[1], 0)

grid = [['#' if (m, n) in walls else '.' for m in range(xbounds[0], xbounds[1]+1)] for n in range(ybounds[0], ybounds[1]+1)]

grid_x_offset = xbounds[0]
grid_y_offset = ybounds[0]

sand_count = 0
while True:
    sand = (500, 0)
    while True:
        if sand[1] >= ybounds[1]:
            print(sand_count)
            exit()
        if grid[sand[1]+1-grid_y_offset][sand[0]-grid_x_offset] == '.':
            sand = (sand[0], sand[1]+1)
        else:
            if grid[sand[1]+1-grid_y_offset][sand[0]-1-grid_x_offset] == '.':
                sand = (sand[0] - 1, sand[1] + 1)
                continue
            if grid[sand[1]+1-grid_y_offset][sand[0]+1-grid_x_offset] == '.':
                sand = (sand[0] + 1, sand[1] + 1)
                continue
            sand_count += 1
            grid[sand[1]-grid_y_offset][sand[0]-grid_x_offset] = 'o'
            break
