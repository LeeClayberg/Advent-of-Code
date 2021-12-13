
points = []
folds = []

reading_in_points = True
# Read in stuff
with open("files/input_13.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        if line == "\n":
            reading_in_points = False
        else:
            if reading_in_points:
                x, y = line[:-1].split(",")
                points.append((int(x), int(y)))
            else:
                eql = line[:-1].split(" ")[-1]
                axis, amount = eql.split("=")
                if axis == "x":
                    folds.append((int(amount), 0))
                else:
                    folds.append((0, int(amount)))

for fold_x, fold_y in folds:
    new_points = []
    for point_x, point_y in points:
        if fold_x == 0:
            if point_y < fold_y:
                new_points.append((point_x, point_y))
            else:
                new_y = (fold_y * 2) - point_y
                new_points.append((point_x, new_y))
        else:
            if point_x < fold_x:
                new_points.append((point_x, point_y))
            else:
                new_x = (fold_x * 2) - point_x
                new_points.append((new_x, point_y))
    points = list(set(new_points))

max_x = max(points, key=lambda p: p[0])[0]
max_y = max(points, key=lambda p: p[1])[1]
code = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]
for x, y in points:
    code[y][x] = True
for row in code:
    print(' '.join(list(map(lambda x: "#" if x else ".", row))))
