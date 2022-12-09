changes = {'U': (0, 1), 'L': (-1, 0), 'R': (1, 0), 'D': (0, -1)}

head = (0, 0)
tail = (0, 0)

positions = set()
positions.add(tail)
# Read in stuff
with open("files/input_09.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        direction, amount = line[:-1].split()

        for _ in range(int(amount)):
            head = (head[0] + changes[direction][0], head[1] + changes[direction][1])

            tail_range = [(tail[0] + a, tail[1] + b) for a in range(-1, 2) for b in range(-1, 2)]
            if head not in tail_range:
                tail = next(pos for pos in tail_range if (pos[0] == head[0] and abs(pos[1] - head[1]) == 1)
                            or (pos[1] == head[1] and abs(pos[0] - head[0]) == 1))
                positions.add(tail)

print(len(positions))
