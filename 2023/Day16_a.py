

with open("files/day16.txt", "r") as file_stream:
    grid = file_stream.readlines()
    grid = [line[:-1] for line in grid]

points = [(0, 0)]
directions = [(1, 0)]
seen = set()
covered = set()
changes = [(1, 0), (0, -1), (-1, 0), (0, 1)]
while len(points) > 0:
    point = points.pop(0)
    direction = directions.pop(0)

    if point[0] < 0 or point[0] >= len(grid[0]) or point[1] < 0 or point[1] >= len(grid):
        continue

    covered.add(point)

    key = (point, direction)
    if key in seen:
        continue
    else:
        seen.add(key)

    spot = grid[point[1]][point[0]]

    if spot == '/':
        if direction[0] == 0:
            idx = (changes.index(direction) - 1) % len(changes)
        else:
            idx = (changes.index(direction) + 1) % len(changes)
        new_direction = changes[idx]
        directions.append(new_direction)
        points.append((point[0] + new_direction[0], point[1] + new_direction[1]))
    elif spot == '\\':
        if direction[0] == 0:
            idx = (changes.index(direction) + 1) % len(changes)
        else:
            idx = (changes.index(direction) - 1) % len(changes)
        new_direction = changes[idx]
        directions.append(new_direction)
        points.append((point[0] + new_direction[0], point[1] + new_direction[1]))
    elif spot == '|' and direction[0] != 0:
        point_1 = (point[0], point[1] - 1)
        direction_1 = (0, -1)
        point_2 = (point[0], point[1] + 1)
        direction_2 = (0, 1)
        points.extend([point_1, point_2])
        directions.extend([direction_1, direction_2])
    elif spot == '-' and direction[1] != 0:
        point_1 = (point[0] - 1, point[1])
        direction_1 = (-1, 0)
        point_2 = (point[0] + 1, point[1])
        direction_2 = (1, 0)
        points.extend([point_1, point_2])
        directions.extend([direction_1, direction_2])
    else:
        points.append((point[0]+direction[0], point[1]+direction[1]))
        directions.append(direction)
print(len(covered))