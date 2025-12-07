import re
# Read in stuff
with open("files/day06.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [re.split('\s+', line[:-1]) for line in lines]

    total = 0
    for idx in range(0, len(lines[0])):
        a, b, c, d, op = int(lines[0][idx]), int(lines[1][idx]), int(lines[2][idx]), int(lines[3][idx]), lines[4][idx]
        if op == '*':
            total += a * b * c * d
        else:
            total += a + b + c + d
    print(total)


