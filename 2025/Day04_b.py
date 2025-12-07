
# Read in stuff
with open("files/day04.txt", "r") as file_stream:
    lines = file_stream.readlines()
    rows = [[item for item in line[:-1]] for line in lines]

    all_removed = []
    sub_removed = None
    while sub_removed is None or len(sub_removed) != 0:
        sub_removed = []
        for y, row in enumerate(rows):
            for x, cell in enumerate(row):
                if rows[y][x] == '@':
                    sub_sub_count = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < len(rows) and 0 <= nx < len(row):
                                if rows[ny][nx] == '@':
                                    sub_sub_count += 1
                    if sub_sub_count <= 4:
                        sub_removed.append((x, y))
        for x, y in sub_removed:
            rows[y][x] = '.'
        all_removed.extend(sub_removed)
    print(len(all_removed))

