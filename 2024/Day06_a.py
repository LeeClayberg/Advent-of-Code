
# Read in stuff
with open("files/day06.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    moves = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    guard = None
    guard_dir_idx = 0
    objects = set()
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == '#':
                objects.add((x, y))
            elif cell == '^':
                guard = (x, y)

    path = set()
    while 0 <= guard[0] < len(lines[0]) and 0 <= guard[1] < len(lines):
        new_guard = (guard[0] + moves[guard_dir_idx % 4][0], guard[1] + moves[guard_dir_idx % 4][1])
        if new_guard in objects:
            guard_dir_idx += 1
            continue
        path.add(guard)
        guard = new_guard
    print(len(path))
