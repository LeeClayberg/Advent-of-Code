
sides = set()
with open("files/input_18.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        x, y, z = [int(v) for v in line[:-1].split(',')]
        for c_x, c_y, c_z in [(0.5, 0, 0), (-0.5, 0, 0), (0, 0.5, 0), (0, -0.5, 0), (0, 0, 0.5), (0, 0, -0.5)]:
            side = (x + c_x, y + c_y, z + c_z)
            if side in sides:
                sides.remove(side)
            else:
                sides.add(side)

print(len(sides))
