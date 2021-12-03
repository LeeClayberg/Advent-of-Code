
grid = []

# Read in stuff
with open("files/input_11.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        grid.append(line[:-1])

for i in range(len(grid)):
    grid[i] = grid[i].replace('L', '#')

round = 0
last = ""
prev = "c"

while last != prev:
    changed = 0
    switch = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] != '.':
                count = 0
                total_count = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if not (x == y and x == 0):
                            gird_i = i + x
                            gird_j = j + y
                            check = False
                            while not (gird_i > len(grid) - 1 or gird_i < 0) and not (gird_j > len(grid[0]) - 1 or gird_j < 0):
                                check = True
                                if grid[gird_i][gird_j] in "#":
                                    count += 1
                                    break
                                if grid[gird_i][gird_j] in "L":
                                    break
                                gird_i += x
                                gird_j += y
                            if check:
                                total_count += 1
                if round % 2 == 0:
                    if count >= 5:
                        switch.append((i, j))
                else:
                    if count == 0:
                        switch.append((i, j))
    for pt in switch:
        grid[pt[0]] = grid[pt[0]][:pt[1]] + ('L' if round % 2 == 0 else '#') + grid[pt[0]][pt[1]+1:]
    round += 1
    last = prev
    prev = ''.join(grid)

total = 0
for row in grid:
    total += row.count('#')
print(total)


