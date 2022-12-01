
rows = []
# Read in stuff
with open("files/input_22test.txt", "r") as file_stream:
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
        rows.append((bool_value, (min(max(x_min, -50), 50), min(max(x_max, -50), 50)), (min(max(y_min, -50), 50), min(max(y_max, -50), 50)), (min(max(z_min, -50), 50), min(max(z_max, -50), 50))))
print(rows)
x_on_list = []
y_on_list = []
z_on_list = []
for value, x_data, y_data, z_data in rows[:21]:
    for on_list, data in [(x_on_list, x_data), (y_on_list, y_data), (z_on_list, z_data)]:
        if value:
            on_list.append(data)
            on_list.sort()
            a = 1
            while a < len(on_list):
                if on_list[a][0] <= on_list[a-1][1]:
                    new_tuple = (on_list[a-1][0], max(on_list[a-1][1], on_list[a][1]))
                    on_list[a-1] = new_tuple
                    on_list.pop(a)
                else:
                    a += 1
        else:
            a = 0
            while a < len(on_list):
                min_h = on_list[a][0] < data[0] < on_list[a][1]
                max_h = on_list[a][0] < data[1] < on_list[a][1]
                if min_h and max_h:
                    part = (data[1] + 1, on_list[a][1])
                    on_list[a] = (on_list[a][0], data[0] - 1)
                    on_list.insert(a + 1, part)
                    break
                elif min_h:
                    on_list[a] = (on_list[a][0], data[0] - 1)
                    a += 1
                elif max_h:
                    on_list[a] = (data[1] + 1, on_list[a][1])
                    a += 1
                elif data[0] <= on_list[a][0] and on_list[a][1] <= data[1]:
                    on_list.pop(a)
                else:
                    a += 1

print(x_on_list)
print(y_on_list)
print(z_on_list)

total = 0
for x_range in x_on_list:
    for y_range in y_on_list:
        for z_range in z_on_list:
            x_dist = abs(x_range[1] - x_range[0]) + 1
            y_dist = abs(y_range[1] - y_range[0]) + 1
            z_dist = abs(z_range[1] - z_range[0]) + 1
            total += x_dist * y_dist * z_dist
print(total)
