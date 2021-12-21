import ast
import math

scanner_values = dict()
# Read in stuff
with open("files/input_19.txt", "r") as file_stream:
    current_key = None
    points = set()
    while True:
        line = file_stream.readline()
        if not line:
            break
        if line == '\n':
            continue
        if line[:3] == "---":
            current_key = int(line[:-1].split(" ")[2])
            scanner_values[current_key] = []
        else:
            x, y, z = line[:-1].split(",")
            scanner_values[current_key].append((int(x), int(y), int(z)))
            points.add((int(x), int(y), int(z)))

relative_scanner_values = dict()
for i in scanner_values.keys():
    all_points = scanner_values[i]
    relative_scanner_values[i] = dict()
    for j, base_point in enumerate(all_points):
        b_x, b_y, b_z = base_point
        rest_of_points = all_points[:j] + all_points[j+1:]
        relative_scanner_values[i][base_point] = set()
        for x, y, z in rest_of_points:
            change_vector = (x-b_x, y-b_y, z-b_z)
            relative_scanner_values[i][base_point].add(change_vector)


def rotation_from_int(point_changes, h_list):
    z_rotate = lambda pnt: (pnt[1], -pnt[0], pnt[2])
    x_rotate = lambda pnt: (pnt[0], -pnt[2], pnt[1])
    y_rotate = lambda pnt: (pnt[2], pnt[1], -pnt[0])
    transformations = [
        [],
        [z_rotate],
        [z_rotate, z_rotate],
        [z_rotate, z_rotate, z_rotate],  # Front
        [x_rotate],
        [x_rotate, z_rotate],
        [x_rotate, z_rotate, z_rotate],
        [x_rotate, z_rotate, z_rotate, z_rotate],  # Bottom
        [x_rotate, x_rotate],
        [x_rotate, x_rotate, z_rotate],
        [x_rotate, x_rotate, z_rotate, z_rotate],
        [x_rotate, x_rotate, z_rotate, z_rotate, z_rotate],  # Back
        [x_rotate, x_rotate, x_rotate],
        [x_rotate, x_rotate, x_rotate, z_rotate],
        [x_rotate, x_rotate, x_rotate, z_rotate, z_rotate],
        [x_rotate, x_rotate, x_rotate, z_rotate, z_rotate, z_rotate],  # Top
        [y_rotate],
        [y_rotate, z_rotate],
        [y_rotate, z_rotate, z_rotate],
        [y_rotate, z_rotate, z_rotate, z_rotate],  # Left
        [y_rotate, y_rotate, y_rotate],
        [y_rotate, y_rotate, y_rotate, z_rotate],
        [y_rotate, y_rotate, y_rotate, z_rotate, z_rotate],
        [y_rotate, y_rotate, y_rotate, z_rotate, z_rotate, z_rotate]  # Right
    ]
    point_list = list(point_changes)
    for h in h_list:
        for rotation in transformations[h]:
            point_list = list(map(rotation, point_list))
    return set(point_list)


def undo_rotation_from_int(point_changes, h_list):
    z_rotate = lambda pnt: (-pnt[1], pnt[0], pnt[2])
    x_rotate = lambda pnt: (pnt[0], pnt[2], -pnt[1])
    y_rotate = lambda pnt: (-pnt[2], pnt[1], pnt[0])
    transformations = [
        [],
        [z_rotate],
        [z_rotate, z_rotate],
        [z_rotate, z_rotate, z_rotate],  # Front
        [x_rotate],
        [x_rotate, z_rotate],
        [x_rotate, z_rotate, z_rotate],
        [x_rotate, z_rotate, z_rotate, z_rotate],  # Bottom
        [x_rotate, x_rotate],
        [x_rotate, x_rotate, z_rotate],
        [x_rotate, x_rotate, z_rotate, z_rotate],
        [x_rotate, x_rotate, z_rotate, z_rotate, z_rotate],  # Back
        [x_rotate, x_rotate, x_rotate],
        [x_rotate, x_rotate, x_rotate, z_rotate],
        [x_rotate, x_rotate, x_rotate, z_rotate, z_rotate],
        [x_rotate, x_rotate, x_rotate, z_rotate, z_rotate, z_rotate],  # Top
        [y_rotate],
        [y_rotate, z_rotate],
        [y_rotate, z_rotate, z_rotate],
        [y_rotate, z_rotate, z_rotate, z_rotate],  # Left
        [y_rotate, y_rotate, y_rotate],
        [y_rotate, y_rotate, y_rotate, z_rotate],
        [y_rotate, y_rotate, y_rotate, z_rotate, z_rotate],
        [y_rotate, y_rotate, y_rotate, z_rotate, z_rotate, z_rotate]  # Right
    ]
    point_list = list(point_changes)
    for h in h_list:
        for rotation in transformations[h]:
            point_list = list(map(rotation, point_list))
    return set(point_list)


same_points = []
linked = dict()
for a in range(len(scanner_values.keys())):
    rest_range = list(range(a)) + list(range(a+1, len(scanner_values.keys())))
    for b in rest_range:
        point_map_1 = relative_scanner_values[a]
        point_map_2 = relative_scanner_values[b]
        for point_1 in point_map_1.keys():
            for point_2 in point_map_2.keys():
                for p in range(24):
                    inter = point_map_1[point_1].intersection(rotation_from_int(point_map_2[point_2], [p]))
                    if len(inter) > 1:
                        same_points.append(((point_1, a), (point_2, b), p))
                        if a not in linked.keys():
                            linked[a] = []
                        linked[a].append((point_1, point_2, b, p))

seen = dict()
queue = [(0, (0, 0, 0), [], [], (0, 0, 0))]
while len(queue) > 0:
    f, total, rotations_1, rotations_2, last_second = queue.pop(0)
    if f not in seen.keys():
        seen[f] = (-total[0], -total[1], -total[2])
        for point_1, point_2, b, p in linked[f]:
            # Between levels
            first = list(rotation_from_int([point_1], rotations_1))[0]
            new_rotations_1 = rotations_1 + [p]
            new_rotations_2 = rotations_2 + [p]
            second = list(rotation_from_int([point_2], new_rotations_2))[0]
            change = (second[0] - first[0], second[1] - first[1], second[2] - first[2])
            path = (total[0] + change[0], total[1] + change[1], total[2] + change[2])
            queue.append((b, path, new_rotations_1, new_rotations_2, second))

largest = 0
l_list = [seen[key] for key in seen.keys()]
for a, point_1 in enumerate(l_list):
    b_x, b_y, b_z = point_1
    rest_of_points = l_list[:a] + l_list[a + 1:]
    for b, point_2 in enumerate(rest_of_points):
        x, y, z = point_2
        largest = max(largest, abs(x-b_x) + abs(y-b_y) + abs(z-b_z))
print(largest)
exit()