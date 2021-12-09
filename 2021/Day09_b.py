from functools import reduce

numbers = []
checked = []
# Read in stuff
with open("files/input_09.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(list(map(lambda x: int(x), line[:-1])))
        checked.append([False for _ in range(len(line)-1)])

# Find low points
low_points = []
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        check = True
        if i > 0:
            check &= (numbers[i][j] < numbers[i-1][j])
        if j > 0:
            check &= (numbers[i][j] < numbers[i][j-1])
        if i < len(numbers) - 1:
            check &= (numbers[i][j] < numbers[i+1][j])
        if j < len(numbers[i]) - 1:
            check &= (numbers[i][j] < numbers[i][j+1])
        if check:
            low_points.append((i, j))

# Sort low points
low_points = sorted(low_points, key=lambda x: numbers[x[0]][x[1]])

# Find basins
basin_sizes = []
for low_point in low_points:
    if not checked[low_point[0]][low_point[1]]:
        queue = [low_point]
        count = 0
        while len(queue) > 0:
            x, y = queue.pop(0)
            if numbers[x][y] < 9 and not checked[x][y]:
                checked[x][y] = True
                count += 1
                if x > 0:
                    queue.append((x - 1, y))
                if y > 0:
                    queue.append((x, y - 1))
                if x < len(numbers) - 1:
                    queue.append((x + 1, y))
                if y < len(numbers[x]) - 1:
                    queue.append((x, y + 1))
        basin_sizes.append(count)

largest_basins = sorted(basin_sizes)[-3:]
print(reduce(lambda x, y: x * y, largest_basins, 1))
