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


def rotation_from_int(point_changes, h):
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
    for rotation in transformations[h]:
        point_list = list(map(rotation, point_list))
    return set(point_list)


same_points = []
for a in range(26):
    rest_range = list(range(a)) + list(range(a+1, 26))
    for b in rest_range:
        point_map_1 = relative_scanner_values[a]
        point_map_2 = relative_scanner_values[b]
        for point_1 in point_map_1.keys():
            for point_2 in point_map_2.keys():
                for p in range(24):
                    inter = point_map_1[point_1].intersection(rotation_from_int(point_map_2[point_2], p))
                    if len(inter) > 1:
                        same_points.append((point_1, point_2))

same_point_groups = []
for p1, p2 in same_points:
    add_new = True
    for i in range(len(same_point_groups)):
        if p1 in same_point_groups[i] or p2 in same_point_groups[i]:
            same_point_groups[i].add(p1)
            same_point_groups[i].add(p2)
            add_new = False
            break
    if add_new:
        same_point_groups.append({p1, p2})

for group in same_point_groups:
    for point in list(group)[1:]:
        points.discard(point)
print(len(points))
