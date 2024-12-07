
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
    start = guard

    path = []
    while 0 <= guard[0] < len(lines[0]) and 0 <= guard[1] < len(lines):
        new_guard = (guard[0] + moves[guard_dir_idx % 4][0], guard[1] + moves[guard_dir_idx % 4][1])
        if new_guard in objects:
            guard_dir_idx += 1
            continue
        path.append((new_guard[0], new_guard[1], guard_dir_idx % 4))
        guard = new_guard

    found = set()
    checked = set()
    for idx, node in enumerate(path[:-1]):
        x, y, rot = node
        guard, new_object = (x, y), (path[idx+1][0], path[idx+1][1])

        if new_object in checked or new_object == start:
            # Already seen or starting position of guard
            continue

        sub_path = [p for p in path[:idx]]
        while 0 <= guard[0] < len(lines[0]) and 0 <= guard[1] < len(lines):
            new_guard = (guard[0] + moves[rot][0], guard[1] + moves[rot][1])
            if new_guard in objects or new_guard == new_object:
                rot = (rot + 1) % 4
                continue
            sub_node = (new_guard[0], new_guard[1], rot)
            if sub_node in sub_path:
                found.add(new_object)
                break
            sub_path.append(sub_node)
            guard = new_guard
        checked.add(new_object)

    print(len(found))