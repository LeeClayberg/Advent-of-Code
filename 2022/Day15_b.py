
sensor_data = dict()
beacons = set()

with open("files/input_15.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        parts = line[:-1].split(" ")
        x = int(parts[2][2:-1])
        y = int(parts[3][2:-1])
        a = int(parts[-2][2:-1])
        b = int(parts[-1][2:])
        sensor = (x, y)
        beacons.add((a, b))
        m_distance = abs(a - x) + abs(b - y)
        sensor_data[sensor] = m_distance

options = dict()
# Get points along border manhattan range
for pos, dist in sensor_data.items():
    border_dist = dist + 1

    top = (pos[0], pos[1] + border_dist)
    for change in range(border_dist):
        if top not in options.keys():
            options[top] = 0
        options[top] += 1
        top = (top[0]+1, top[1]-1)

    bottom = (pos[0], pos[1] - border_dist)
    for change in range(border_dist):
        if bottom not in options.keys():
            options[bottom] = 0
        options[bottom] += 1
        bottom = (bottom[0]-1, bottom[1]+1)

    left = (pos[0] - border_dist, pos[1])
    for change in range(border_dist):
        if left not in options.keys():
            options[left] = 0
        options[left] += 1
        left = (left[0]+1, left[1]+1)

    right = (pos[0] + border_dist, pos[1])
    for change in range(border_dist):
        if right not in options.keys():
            options[right] = 0
        options[right] += 1
        right = (right[0]-1, right[1]-1)

# Find point in options that is barely out of range for four sensors
filtered_options = [pos for pos, count in options.items() if count >= 4]
for option in filtered_options:
    if 0 <= option[0] <= 4000000 and 0 <= option[1] <= 4000000:
        tuning_freq = option[0] * 4000000 + option[1]
        print(tuning_freq)
        exit()
