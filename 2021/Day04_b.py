from functools import reduce

calls = []
boards = []
# Read in stuff
with open("files/input_04.txt", "r") as file_stream:
    line = file_stream.readline()
    calls = list(map(lambda x: int(x), line.split(",")))

    while True:
        line = file_stream.readline()
        if not line:
            break
        board = []
        for _ in range(5):
            line = file_stream.readline()
            row = (list(map(lambda x: [int(x), False], line.split())))
            board.append(row)
        boards.append(board)

for call in calls:
    boards_to_remove = set()
    for k, board in enumerate(boards):
        # Mark board
        for row in board:
            for value in row:
                if value[0] == call:
                    value[1] = True
        # Check board (rows)
        for i in range(len(board)):
            if reduce(lambda total, val: total and val[1], board[i], True):
                # Board found
                boards_to_remove.add(k)
                if len(boards) == 1:
                    flat_list = [item for row in board for item in row]
                    score = reduce(lambda total, val: total + (0 if val[1] else val[0]), flat_list, 0)
                    print(score * call)
                    exit()
        # Check board (columns)
        for i in range(len(board)):
            if reduce(lambda total, val: total and val[1], list(map(lambda r: r[i], board)), True):
                # Board found
                boards_to_remove.add(k)
                if len(boards) == 1:
                    flat_list = [item for row in board for item in row]
                    score = reduce(lambda total, val: total + (0 if val[1] else val[0]), flat_list, 0)
                    print(score * call)
                    exit()

    for remove_index in reversed(sorted(list(boards_to_remove))):
        boards.pop(remove_index)
