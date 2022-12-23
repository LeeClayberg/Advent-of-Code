
# parse grid
grid = []
with open("files/input_23.txt", "r") as file_stream:
    width = 0
    while True:
        line = file_stream.readline()
        if not line:
            break
        grid.append(list(line[:-1]))

# create elves
elves = []
for y, row in enumerate(grid):
    for x, entry in enumerate(row):
        if entry == '#':
            elves.append((x, y, ['N', 'S', 'W', 'E']))

north = [(-1, -1), (0, -1), (1, -1)]
south = [(-1, 1), (0, 1), (1, 1)]
east = [(1, 1), (1, 0), (1, -1)]
west = [(-1, 1), (-1, 0), (-1, -1)]
dir_changes = dict({'N': north, 'S': south, 'E': east, 'W': west})
dir_update = dict({'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)})
changes = set(north + south + east + west)
r = 0
while True:
    r += 1
    filled = set([(x, y) for x, y, _ in elves])

    # first half
    updated_elves = []
    proposed = []
    counter = dict()
    exit_check = True
    for x, y, directions in elves:
        # initial check
        if all([(x + c_x, y + c_y) not in filled for c_x, c_y in changes]):
            updated_elves.append((x, y, directions[1:] + directions[:1]))
            exit_check &= True
            continue
        exit_check &= False
        # check directions
        found = False
        for d in directions:
            if all([(x + c_x, y + c_y) not in filled for c_x, c_y in dir_changes[d]]):
                update_x, update_y = (x + dir_update[d][0], y + dir_update[d][1])
                proposed.append((x, y, directions, d, update_x, update_y))
                if (update_x, update_y) not in counter.keys():
                    counter[(update_x, update_y)] = 0
                counter[(update_x, update_y)] += 1
                found = True
                break
        # no moves
        if not found:
            updated_elves.append((x, y, directions[1:] + directions[:1]))

    if exit_check:
        break

    # second half
    for x, y, directions, d, p_x, p_y in proposed:
        new_directions = directions[1:] + directions[:1]
        if counter[(p_x, p_y)] > 1:
            # cross over, don't do anything
            updated_elves.append((x, y, new_directions))
        else:
            # move to new place
            updated_elves.append((p_x, p_y, new_directions))

    elves = updated_elves

print(r)
