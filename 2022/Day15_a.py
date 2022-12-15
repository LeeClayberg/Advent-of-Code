
sensor_data = dict()
beacons = set()
line_y = 2000000
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

# Get ranges where manhattan distance would reach
on_line = set()
for pos, dist in sensor_data.items():
    line_min = abs(pos[1] - line_y)
    if line_min > dist:
        # Fully outside range
        continue

    horizontal_dist = dist - line_min
    for x in range(pos[0]-horizontal_dist, pos[0]+horizontal_dist+1):
        on_line.add((x, line_y))

# Exclude beacons and senors possibly on that line
excluding_beacons = on_line.difference(beacons)
excluding_sensors = excluding_beacons.difference(set(sensor_data.keys()))
print(len(excluding_sensors))
