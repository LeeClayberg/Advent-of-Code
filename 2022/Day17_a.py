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
    for h in reversed(range(board_h)):
        row = ""
        for a in range(7):
            row += "#" if (a, h) in s else "."
        tower += f"|{row}|\n"
    tower += "+-------+\n\n"
    print(tower)


with open("files/input_17.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        movement = [-1 if c == '<' else 1 for c in list(line[:-1])]

        stationary = set()
        m = 0
        for r in range(2022):
            piece = copy.deepcopy(pieces[r % len(pieces)])
            height = max(stationary, key=lambda p: p[1], default=(0, -1))[1] + 1
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

            stationary.update(set(piece))
            # print_board(stationary)
        print(max(stationary, key=lambda p: p[1])[1] + 1)
