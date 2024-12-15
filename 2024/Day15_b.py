
# Read in stuff
with open("files/day15.txt", "r") as file_stream:
    # Setup
    grid, moves = file_stream.read().split('\n\n')
    move_map = {'^': (0, -1), '<': (-1, 0), '>': (1, 0), 'v': (0, 1)}
    walls = set()
    boxes = {}
    robot = None
    for y, row in enumerate(grid.split('\n')):
        for x, cell in enumerate(row):
            x1, x2 = x * 2, x * 2 + 1
            if cell == '#':
                walls.add((x1, y))
                walls.add((x2, y))
            elif cell == 'O':
                boxes[(x1, y)] = (x2, y)
                boxes[(x2, y)] = (x1, y)
            elif cell == '@':
                robot = (x1, y)
    moves = [move_map[move] for move in moves.replace('\n', '')]

    # Moves: TODO
    for dx, dy in moves:
        rx, ry = robot
        new_robot = (rx + dx, ry + dy)
        if new_robot in walls:
            continue
        elif new_robot in boxes:
            to_check = [new_robot, boxes[new_robot]]
            visited = []
            can_move = True
            while len(to_check) > 0:
                check = to_check.pop(0)
                if check in visited:
                    continue
                new_check = (check[0] + dx, check[1] + dy)
                if new_check in walls:
                    can_move = False
                    break
                elif new_check in boxes:
                    to_check.append(new_check)
                    to_check.append(boxes[new_check])
                visited.append(check)
            if can_move:
                robot = new_robot
                for box in reversed(visited):
                    old_value = boxes[box]
                    del boxes[box]
                    boxes[(box[0]+dx, box[1]+dy)] = (old_value[0]+dx, old_value[1]+dy)
        else:
            robot = new_robot

        # grid_str = ""
        # for y in range(0, len(grid.split('\n'))):
        #     row_str = ""
        #     for x in range(0, len(row) * 2):
        #         if (x, y) in walls:
        #             row_str += "#"
        #         elif (x, y) in boxes.keys():
        #             row_str += "O"
        #         elif (x, y) == robot:
        #             row_str += "@"
        #         else:
        #             row_str += "."
        #     grid_str += row_str + '\n'
        # print(grid_str)
        # print()

    # Count
    total = 0
    for box_part in boxes.keys():
        other_box_part = boxes[box_part]
        if box_part[0] > other_box_part[0]:
            continue
        x, y = box_part
        total += y * 100 + x
    print(total)

