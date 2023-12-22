

with open("files/day18.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

point = (0, 0)

border = set()
values = set()

for line in lines:
    direction, amount, color = line.split(' ')
    amount = int(amount)
    color = color[2:-1]

    change = directions[direction]
    new_border = [(point[0] + (change[0] * i), point[1] + (change[1] * i)) for i in range(0, amount+1)]
    border.update(new_border)



    point = (point[0]+(change[0] * amount), point[1]+(change[1] * amount))

top_left_corner = (min(spot[0] for spot in border)-2, min(spot[1] for spot in border)-2)
bottom_right_corner = (max(spot[0] for spot in border)+2, max(spot[1] for spot in border)+2)

inside = False
top = None
inside_hole = border.copy()
for y in range(top_left_corner[1], bottom_right_corner[1]+1):
    for x in range(top_left_corner[0], bottom_right_corner[0]+1):
        if (x, y) in border:
            if (x-1, y) not in border and (x+1, y) not in border:
                inside = not inside
            elif not((x-1, y) in border and (x+1, y) in border):
                if top is None:
                    top = (x, y-1) in border
                else:
                    if (top and (x, y-1) not in border) or (not top and (x, y-1) in border):
                        inside = not inside
                    top = None
        else:
            if inside:
                inside_hole.add((x, y))
print(len(inside_hole))
