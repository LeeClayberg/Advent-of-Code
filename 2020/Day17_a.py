lines = []

# Read in stuff
with open("files/input_17.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

positions = dict()

for x, line in enumerate(lines):
    for y, val in enumerate(line):
        positions[(x, y, 0)] = val == '#'

for cycle in range(0, 6):
    all_x = list(map(lambda x: x[0], positions))
    all_y = list(map(lambda x: x[1], positions))
    all_z = list(map(lambda x: x[2], positions))

    range_positions = [(x, y, z) for z in range(min(all_z)-1, max(all_z)+2) for y in range(min(all_y)-1, max(all_y)+2) for x in range(min(all_x)-1, max(all_x)+2)]

    for point in range_positions:
        if point not in positions.keys():
            positions[point] = False

    set_to_active = set()
    set_to_inactive = set()
    for position in positions.keys():
        neighbors = [(x, y, z) for z in range(position[2]-1, position[2]+2) for y in range(position[1]-1, position[1]+2) for x in range(position[0]-1, position[0]+2)]
        active = 0
        for point in neighbors:
            if point != position and point in positions.keys() and positions[point]:
                active += 1
        if positions[position] and not (active == 2 or active == 3):
            set_to_inactive.add(position)
        if not positions[position] and active == 3:
            set_to_active.add(position)

    for point in set_to_active:
        positions[point] = True
    for point in set_to_inactive:
        positions[point] = False

total_active = 0
for point in positions.keys():
    if positions[point]:
        total_active += 1
print(total_active)
