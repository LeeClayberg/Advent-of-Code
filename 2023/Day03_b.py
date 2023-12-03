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
            if spot == '*':
                symbols.append((row, col))
            if len(current_group) > 0:
                groups.append(current_group)
                current_group = []
    if len(current_group) > 0:
        groups.append(current_group)
        current_group = []

gear_ratios = []
for symbol in symbols:
    adjacent_groups = []
    for group in groups:
        for num in group:
            if abs(num[0] - symbol[0]) <= 1 and abs(num[1] - symbol[1]) <= 1:
                adjacent_groups.append(group)
                break
    if len(adjacent_groups) == 2:
        gear_ratios.append(adjacent_groups)

total = 0
for gear_ratio in gear_ratios:
    first_num = ''
    for num in gear_ratio[0]:
        first_num += num[2]
    second_num = ''
    for num in gear_ratio[1]:
        second_num += num[2]
    total += (int(first_num) * int(second_num))
print(total)