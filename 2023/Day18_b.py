

# From online
def ccw(a,b,c):
    return (c[1]-a[1]) * (b[0]-a[0]) > (b[1]-a[1]) * (c[0]-a[0])
def intersect(a,b,c,d):
    return ccw(a,c,d) != ccw(b,c,d) and ccw(a,b,c) != ccw(a,b,d)

with open("files/day18.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
additions = {
    ('U', 'R'): (-0.5, -0.5),
    ('U', 'L'): (-0.5, 0.5),
    ('D', 'R'): (0.5, -0.5),
    ('D', 'L'): (0.5, 0.5),
    ('L', 'U'): (-0.5, 0.5),
    ('L', 'D'): (0.5, 0.5),
    ('R', 'U'): (-0.5, -0.5),
    ('R', 'D'): (0.5, -0.5),
}

point = (0, 0)

border = []
border_directions = []
verticals = []

for line in lines:
    direction, amount, color = line.split(' ')
    color = color[2:-1]
    amount, direction = color[:-1], color[-1]
    amount = int(amount, 16)
    direction = int(direction)
    direction = ['R', 'D', 'L', 'U'][direction]
    amount = int(amount)

    change = directions[direction]

    new_x, new_y = point[0]+(change[0] * amount), point[1]+(change[1] * amount)
    point = (new_x, new_y)
    border.append(point)
    border_directions.append(direction)

new_border = []
for _ in range(0, len(border)):
    point = border[0]
    dir_1, dir_2 = border_directions[0], border_directions[1]
    change = additions[(dir_1, dir_2)]
    new_border.append((point[0]+change[0], point[1]+change[1]))

    border.append(border.pop(0))
    border_directions.append(border_directions.pop(0))
size = 0

border = new_border

while len(border) > 2:
    edges = []
    for _ in range(0, len(border)):
        first, second = border[0], border[1]
        edges.append((first, second))
        border.append(border.pop(0))
    for _ in range(0, len(border)):
        first, second, third = border[0], border[1], border[2]
        centroid = ((first[0]+second[0]+third[0]) / 3, (first[1]+second[1]+third[1]) / 3)
        count = 0
        for start, end in edges:
            if intersect((-1000000000000, centroid[0]), centroid, start, end):
                count += 1
        crosses = False
        for start, end in edges:
            if first not in [start, end] and third not in [start, end] and intersect(first, third, start, end):
                crosses = True
                break
        if count % 2 == 1 and not crosses:
            x1, y1 = first
            x2, y2 = second
            x3, y3 = third
            size += 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            border.remove(second)
            break
        border.append(border.pop(0))
print(int(size))
