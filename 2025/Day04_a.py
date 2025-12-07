
# Read in stuff
with open("files/day04.txt", "r") as file_stream:
    lines = file_stream.readlines()
    rows = [line[:-1] for line in lines]

    count = 0
    for y, row in enumerate(rows):
        for x, cell in enumerate(row):
            if rows[y][x] == '@':
                sub_count = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < len(rows) and 0 <= nx < len(row):
                            if rows[ny][nx] == '@':
                                sub_count += 1
                if sub_count <= 4:
                    count += 1
    print(count)

