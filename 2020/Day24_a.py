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
count_black = len(list(filter(lambda x: x, list(spots.values()))))
print(count_black)