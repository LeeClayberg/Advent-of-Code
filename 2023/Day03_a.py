with open("files/day03.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

groups = []
symbols = []
for row, line in enumerate(lines):
    current_group = []
    for col, spot in enumerate(line):
        if spot.isnumeric():
            current_group.append((row, col, spot))
        else:
            if spot != '.':
                symbols.append((row, col))
            if len(current_group) > 0:
                groups.append(current_group)
                current_group = []
    if len(current_group) > 0:
        groups.append(current_group)
        current_group = []

adjacent_groups = []
for group in groups:
    check = False
    for symbol in symbols:
        for num in group:
            if abs(num[0] - symbol[0]) <= 1 and abs(num[1] - symbol[1]) <= 1:
                adjacent_groups.append(group)
                check = True
                break
        if check:
            break

total = 0
for group in adjacent_groups:
    full_num = ''
    for num in group:
        full_num += num[2]
    total += int(full_num)
print(total)