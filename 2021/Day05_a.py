
lines = []
# Read in stuff
with open("files/input_05.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        p1, p2 = line[:-1].split(" -> ")
        lines.append((list(map(lambda x: int(x), p1.split(","))), list(map(lambda x: int(x), p2.split(",")))))

points = dict()
for line in lines:
    # Non-horizontal and Non-vertical
    if line[0][0] != line[1][0] and line[0][1] != line[1][1]:
        continue

    if line[0][0] == line[1][0]:
        min_y, max_y = sorted([line[0][1], line[1][1]])
        for val_y in range(min_y, max_y+1):
            key = str(line[0][0]) + "," + str(val_y)
            if key not in points.keys():
                points[key] = 0
            points[key] += 1
    else:
        min_x, max_x = sorted([line[0][0], line[1][0]])
        for val_x in range(min_x, max_x+1):
            key = str(val_x) + "," + str(line[0][1])
            if key not in points.keys():
                points[key] = 0
            points[key] += 1
print(len(list(filter(lambda x: x > 1, points.values()))))