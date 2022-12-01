
rows = []
# Read in stuff
with open("files/input_22.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        value, ranges = line[:-1].split()
        bool_value = value == "on"
        x_equal, y_equal, z_equal = ranges.split(",")
        x_min, x_max = list(map(lambda x: int(x), x_equal[2:].split("..")))
        y_min, y_max = list(map(lambda y: int(y), y_equal[2:].split("..")))
        z_min, z_max = list(map(lambda z: int(z), z_equal[2:].split("..")))
        rows.append((bool_value, (x_min, x_max), (y_min, y_max), (z_min, z_max)))

on_points = set()
for value, x_data, y_data, z_data in rows:
    x_range = range(max(-50, x_data[0]), min(50, x_data[1])+1)
    y_range = range(max(-50, y_data[0]), min(50, y_data[1])+1)
    z_range = range(max(-50, z_data[0]), min(50, z_data[1])+1)
    for x_val in x_range:
        for y_val in y_range:
            for z_val in z_range:
                block = (x_val, y_val, z_val)
                if value:
                    on_points.add(block)
                else:
                    if block in on_points:
                        on_points.remove(block)
print(len(on_points))
