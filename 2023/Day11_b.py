
with open("files/day11.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

multiplier = 999999

galaxies = []
for a, row in enumerate(lines):
    for b, cell in enumerate(row):
        if cell == '#':
            galaxies.append((a, b))

expand_rows = set()
for i, line in enumerate(lines):
    if all([cell == '.' for cell in line]):
        expand_rows.add(i)

expand_cols = set()
for i in range(0, len(lines[0])):
    if all([lines[j][i] == '.' for j in range(0, len(lines))]):
        expand_cols.add(i)

lengths = {}
for galaxy_a in galaxies:
    for galaxy_b in galaxies:
        if galaxy_a == galaxy_b:
            continue
        key = str(sorted([galaxy_a, galaxy_b]))
        if key in lengths:
            continue

        sub_length = abs(galaxy_a[0] - galaxy_b[0]) + abs(galaxy_a[1] - galaxy_b[1])

        min_h, max_h = min(galaxy_a[0], galaxy_b[0]), max(galaxy_a[0], galaxy_b[0])
        sub_length += len(expand_rows.intersection(set(range(min_h, max_h + 1)))) * multiplier

        min_w, max_w = min(galaxy_a[1], galaxy_b[1]), max(galaxy_a[1], galaxy_b[1])
        sub_length += len(expand_cols.intersection(set(range(min_w, max_w + 1)))) * multiplier
        lengths[key] = sub_length

total = sum(lengths.values())
print(total)
