
# parse grid
blizzards = []
with open("files/input_24.txt", "r") as file_stream:
    y = -2
    while True:
        y += 1
        line = file_stream.readline()
        if not line:
            break
        if len(set(list(line[:-1]))) == 2:
            continue
        inner = line[1:-2]
        for x, pos in enumerate(inner):
            if pos != '.':
                blizzards.append((x, y, pos))

x_bound = max(blizzards, key=lambda r: r[0])[0] + 1
y_bound = max(blizzards, key=lambda r: r[1])[1] + 1

directions = dict({'^': (0, -1), '<': (-1, 0), '>': (1, 0), 'v': (0, 1)})


start = (0, -1)
end = (x_bound-1, y_bound)

parts = [(start, end), (end, start), (start, end)]

total_trip = 0
for s, e in parts:
    check_cache = dict()
    position_cache = dict()

    position_cache[-1] = blizzards
    reached = set()

    queue = [(s[0], s[1], 0)]
    while len(queue) > 0:
        q, w, minute = queue.pop(0)
        if minute > 500 or (q, w, minute) in reached:
            continue
        reached.add((q, w, minute))
        if minute not in check_cache.keys():
            check_blizzards = set()
            updated_blizzards = []
            for a, b, d in position_cache[minute-1]:
                c_a, c_b = directions[d]
                check_blizzards.add(((a + c_a) % x_bound, (b + c_b) % y_bound))
                updated_blizzards.append(((a + c_a) % x_bound, (b + c_b) % y_bound, d))
            check_cache[minute] = check_blizzards
            position_cache[minute] = updated_blizzards
        blizzard_checks = check_cache[minute]

        found = False
        for change in [(1, 0), (0, 1), (0, 0), (0, -1), (-1, 0)]:
            new_position = (q + change[0], w + change[1])
            if new_position in blizzard_checks:
                continue
            if new_position == e:
                total_trip += minute+1
                blizzards = position_cache[minute]
                found = True
                break
            if new_position != start and (not (0 <= new_position[0] < x_bound) or not (0 <= new_position[1] < y_bound)):
                continue
            queue.append((new_position[0], new_position[1], minute+1))
        if found:
            break

print(total_trip)
