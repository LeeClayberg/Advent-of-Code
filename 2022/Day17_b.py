import copy

long = {(2, 3), (3, 3), (4, 3), (5, 3)}
cross = {(2, 4), (3, 4), (3, 5), (3, 3), (4, 4)}
l = {(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)}
tall = {(2, 3), (2, 4), (2, 5), (2, 6)}
square = {(2, 3), (3, 3), (2, 4), (3, 4)}

pieces = [long, cross, l, tall, square]


def print_board(s):
    board_h = max(s, key=lambda p: p[1])[1] + 1
    tower = ""
    for h in reversed(range(board_h - 20, board_h+1)):
        row = ""
        for a in range(7):
            row += "#" if (a, h) in s else "."
        tower += f"|{row}|\n"
    print(tower)


with open("files/input_17.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        movement = [-1 if c == '<' else 1 for c in list(line[:-1])]

        stationary = set()
        m = 0
        height = 0
        for r in range(1000000):
            piece = copy.deepcopy(pieces[r % len(pieces)])
            r += 1
            piece = [(x, y + height) for x, y in piece]
            while True:
                move = movement[m % len(movement)]
                m += 1

                if all((x + move, y) not in stationary and 6 >= x + move >= 0 for x, y in piece):
                    piece = [(x + move, y) for x, y in piece]

                if any((x, y - 1) in stationary or y == 0 for x, y in piece):
                    break
                else:
                    piece = [(x, y - 1) for x, y in piece]

            height = max(height, max([f[1] for f in piece]) + 1)
            stationary.update(set(piece))
            stationary = {e for e in stationary if e[1] > height - 30}
        print(height)
