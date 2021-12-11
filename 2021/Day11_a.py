
numbers = []
# Read in stuff
with open("files/input_11.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(list(map(lambda x: int(x), line[:-1])))

flash_count = 0
for _ in range(100):
    queue = []
    # Increase all values
    for a in range(len(numbers)):
        for b in range(len(numbers[a])):
            numbers[a][b] += 1
            if numbers[a][b] > 9:
                queue.append((a, b))

    # Flow for maxed values
    flashed = [[False for _ in range(len(x))] for x in numbers]
    while len(queue) > 0:
        a, b = queue.pop(0)
        if not flashed[a][b]:
            flashed[a][b] = True
            flash_count += 1
            for c, d in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                e, f = a+c, b+d
                if e not in range(len(numbers)) or f not in range(len(numbers)):
                    continue
                numbers[e][f] += 1
                if numbers[e][f] > 9:
                    queue.append((e, f))

    # Reset for flashed
    for a in range(len(numbers)):
        for b in range(len(numbers[a])):
            if flashed[a][b]:
                numbers[a][b] = 0
print(flash_count)


