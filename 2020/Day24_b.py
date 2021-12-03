lines = []

# Read in stuff
with open("files/input_24.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])


def split_line(line):
    current_idx = 0
    parts = []
    while current_idx < len(line):
        if line[current_idx] in "ew":
            parts.append(line[current_idx])
            current_idx += 1
        else:
            parts.append(line[current_idx:current_idx+2])
            current_idx += 2
    return parts

spots = dict()
for line in lines:
    point = [0, 0]
    for part in split_line(line):
        if part == 'e':
            point[0] += 2
        elif part == 'se':
            point[0] += 1
            point[1] -= 1.5
        elif part == 'sw':
            point[0] -= 1
            point[1] -= 1.5
        elif part == 'w':
            point[0] -= 2
        elif part == 'nw':
            point[0] -= 1
            point[1] += 1.5
        elif part == 'ne':
            point[0] += 1
            point[1] += 1.5
    act_point = (point[0], point[1])
    if act_point in spots.keys():
        spots[act_point] = not spots[act_point]
    else:
        spots[act_point] = True # True is black

for _ in range(0, 100):
    white_possibilties = set(spots.keys())
    # all black tiles which will switch
    black_switchs = []
    for key in spots.keys():
        if spots[key]:
            count = 0
            for change in [(2, 0), (1, -1.5), (-1, -1.5), (-2, 0), (-1, 1.5), (1, 1.5)]:
                new_key = (key[0] + change[0], key[1] + change[1])
                if new_key in spots.keys() and spots[new_key]:
                    count += 1
                white_possibilties.add(new_key)
            if count == 0 or count > 2:
                black_switchs.append(key)
    # all white tiles which will switch
    white_switches = []
    for tile in white_possibilties:
        if tile not in spots.keys() or not spots[tile]:
            count = 0
            for change in [(2, 0), (1, -1.5), (-1, -1.5), (-2, 0), (-1, 1.5), (1, 1.5)]:
                new_key = (tile[0] + change[0], tile[1] + change[1])
                if new_key in spots.keys() and spots[new_key]:
                    count += 1
            if count == 2:
                white_switches.append(tile)
    # switch all tiles
    for tile in black_switchs:
        spots[tile] = False
    for tile in white_switches:
        spots[tile] = True
print(len(list(filter(lambda x: x, list(spots.values())))))
