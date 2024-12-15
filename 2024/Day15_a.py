
# Read in stuff
with open("files/day15.txt", "r") as file_stream:
    # Setup
    grid, moves = file_stream.read().split('\n\n')
    move_map = {'^': (0, -1), '<': (-1, 0), '>': (1, 0), 'v': (0, 1)}
    walls = set()
    boxes = set()
    robot = None
    for y, row in enumerate(grid.split('\n')):
        for x, cell in enumerate(row):
            if cell == '#':
                walls.add((x, y))
            elif cell == 'O':
                boxes.add((x, y))
            elif cell == '@':
                robot = (x, y)
    moves = [move_map[move] for move in moves.replace('\n', '')]

    # Moves:
    for dx, dy in moves:
        rx, ry = robot
        new_robot = (rx + dx, ry + dy)
        if new_robot in walls:
            continue
        elif new_robot in boxes:
            check = new_robot
            can_move = True
            while True:
                new_check = (check[0] + dx, check[1] + dy)
                if new_check in walls:
                    can_move = False
                    break
                else:
                    check = new_check
                    if new_check not in boxes:
                        break
            if can_move:
                robot = new_robot
                boxes.remove(new_robot)
                boxes.add(check)
        else:
            robot = new_robot

    # Count
    total = 0
    for x, y in boxes:
        total += y * 100 + x
    print(total)

