import math

full_tail = [(0, 0) for _ in range(10)]


# Helper for displaying
def print_grid():
    xmin, xmax = min([z[0] for z in full_tail]), max([z[0] for z in full_tail])
    ymin, ymax = min([z[1] for z in full_tail]), max([z[1] for z in full_tail])
    grid = [["." for _ in range(xmin, xmax+1)] for _ in range(ymin, ymax+1)]
    for i, pos in enumerate(full_tail):
        grid[pos[1]-ymin][pos[0]-xmin] = str(i)
    for row in grid[::-1]:
        print(''.join(row))
    print()


changes = {'U': (0, 1), 'L': (-1, 0), 'R': (1, 0), 'D': (0, -1)}

positions = set()
positions.add((0, 0))
# Read in stuff
with open("files/input_09.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        direction, amount = line[:-1].split()

        for _ in range(int(amount)):
            full_tail[0] = (full_tail[0][0] + changes[direction][0], full_tail[0][1] + changes[direction][1])

            for i in range(1, len(full_tail)):
                tail = full_tail[i]
                new_head = full_tail[i-1]

                tail_range = [(tail[0] + a, tail[1] + b) for a in range(-1, 2) for b in range(-1, 2)]
                if new_head not in tail_range:
                    if new_head[0] == tail[0]:
                        full_tail[i] = (tail[0], tail[1]+1 if new_head[1] > tail[1] else tail[1]-1)
                    elif new_head[1] == tail[1]:
                        full_tail[i] = (tail[0]+1 if new_head[0] > tail[0] else tail[0]-1, tail[1])
                    else:
                        for x, y in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
                            check = (new_head[0]-x, new_head[1]-y)
                            if check in tail_range:
                                full_tail[i] = (tail[0] + x, tail[1] + y)
                    if i == 9:
                        positions.add(full_tail[i])
        print_grid()

print(len(positions))
