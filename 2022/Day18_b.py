
sides = set()
active = set()
with open("files/input_18.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        x, y, z = [int(v) for v in line[:-1].split(',')]
        active.add((x, y, z))
        for c_x, c_y, c_z in [(0.5, 0, 0), (-0.5, 0, 0), (0, 0.5, 0), (0, -0.5, 0), (0, 0, 0.5), (0, 0, -0.5)]:
            side = (x + c_x, y + c_y, z + c_z)
            if side in sides:
                sides.remove(side)
            else:
                sides.add(side)

min_x = int(min(sides, key=lambda s: s[0])[0])-1
max_x = int(max(sides, key=lambda s: s[0])[0])+1
min_y = int(min(sides, key=lambda s: s[1])[1])-1
max_y = int(max(sides, key=lambda s: s[1])[1])+1
min_z = int(min(sides, key=lambda s: s[2])[2])-1
max_z = int(max(sides, key=lambda s: s[2])[2])+1

start = (min_x, min_y, min_z)
queue = [start]
seen = set()
outside = set()
while len(queue) > 0:
    a, b, c = queue.pop(0)
    if (a, b, c) in seen or (a, b, c) in active:
        continue
    seen.add((a, b, c))
    # sides
    for c_x, c_y, c_z in [(0.5, 0, 0), (-0.5, 0, 0), (0, 0.5, 0), (0, -0.5, 0), (0, 0, 0.5), (0, 0, -0.5)]:
        side = (a + c_x, b + c_y, c + c_z)
        if side in sides:
            outside.add(side)
    # cubes
    for c_x, c_y, c_z in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
        cube = (a + c_x, b + c_y, c + c_z)
        if min_x <= cube[0] <= max_x and min_y <= cube[1] <= max_y and min_z <= cube[2] <= max_z:
            queue.append(cube)

print(len(outside))
