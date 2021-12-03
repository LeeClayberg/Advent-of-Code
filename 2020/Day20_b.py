from functools import reduce
import numpy as np

lines = []

# Read in stuff
with open("files/input_20.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

picture_size = 12

pieces = dict()
actual_pieces = dict()
current_tile = []
current_id = ""
for line in lines:
    if line[:4] == "Tile":
        current_id = line[5:9]
    elif line == "":
        top = ''.join(current_tile[0])
        bottom = ''.join(current_tile[-1])
        left = ''.join(list(map(lambda x: x[0], current_tile)))
        right = ''.join(list(map(lambda x: x[-1], current_tile)))
        pieces[current_id] = {'top': top, 'bottom': bottom, 'left': left, 'right': right}
        actual_pieces[current_id] = current_tile
        current_tile = []
    else:
        current_tile.append(list(line))

ones_touching = dict()
for key in pieces.keys():
    key_list = list(pieces.keys())
    key_list.remove(key)
    edge_matches = []
    for check_key in key_list:
        all_piece_sides = list(pieces[key].values())
        check_piece_sides = list(pieces[check_key].values()) + list(map(lambda x: x[::-1], list(pieces[check_key].values())))
        side_connected = ["top", "bottom", "left", "right", "topb", "bottomb", "leftb", "rightb"]
        has_match = list(set(all_piece_sides).intersection(set(check_piece_sides)))
        if len(has_match) > 0:
            edge_matches.append({"id": check_key, "side": list(pieces[key].keys())[list(pieces[key].values()).index(has_match[0])],
                                 "side_connected": side_connected[check_piece_sides.index(has_match[0])]})
    ones_touching[key] = {"id": key, "em": edge_matches}
corners = list(filter(lambda x: len(x["em"]) == 2, ones_touching.values()))
corner_ids = list(map(lambda x: int(x["id"]), corners))
corners = list(filter(lambda x: len(x["em"]) == 2, ones_touching.values()))
start_piece = list(filter(lambda x: all(h in list(map(lambda y: y["side"], x["em"])) for h in ['right', 'bottom']), corners))[0]

# add piece spin directions
grid = dict()


def add_piece(point, id, piece):
    grid[point] = piece
    current_piece = np.array(piece)
    actual_pieces.pop(id, None)
    if point[0] < picture_size-1 and (point[0] + 1, point[1]) not in grid.keys():
        check = False
        for key_id in actual_pieces.keys():
            new_piece = np.array(actual_pieces[key_id])
            for _ in range(0, 4):
                for _ in range(0, 2):
                    if np.array_equal(current_piece[:, -1], new_piece[:, 0]):
                        add_piece((point[0] + 1, point[1]), key_id, new_piece)
                        check = True
                    if check:
                        break
                    new_piece = np.flipud(new_piece)
                if check:
                    break
                new_piece = np.rot90(new_piece)
            if check:
                break
    if point[1] < picture_size-1 and (point[0], point[1] + 1) not in grid.keys():
        check = False
        for key_id in actual_pieces.keys():
            new_piece = np.array(actual_pieces[key_id])
            for _ in range(0, 4):
                for _ in range(0, 2):
                    if np.array_equal(current_piece[-1, :], new_piece[0, :]):
                        add_piece((point[0], point[1] + 1), key_id, new_piece)
                        check = True
                    if check:
                        break
                    new_piece = np.flipud(new_piece)
                if check:
                    break
                new_piece = np.rot90(new_piece)
            if check:
                break


add_piece((0, 0), start_piece["id"], np.array(actual_pieces[start_piece["id"]]))

full_picture = []
for grid_r in range(picture_size):
    for grid_r2 in range(1, picture_size-3):
        row = []
        for grid_c in range(picture_size):
            row += grid[(grid_c, grid_r)][grid_r2, 1:-1].tolist()
        full_picture.append(row)
full_picture = np.array(full_picture)

sea_monters = 0
monster_spots = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
for _ in range(0, 4):
    for _ in range(0, 2):
        for i in range(full_picture.shape[0]-20):
            for j in range(full_picture.shape[1] - 3):
                spots = list(map(lambda x: (i+x[0], j+x[1]), monster_spots))
                if all(full_picture[point[0], point[1]] == '#' for point in spots):
                    sea_monters += 1
        full_picture = np.flipud(full_picture)
    full_picture = np.rot90(full_picture)

total = 0
for row in full_picture:
    total += len(list(filter(lambda x: x == '#', row)))
print(total - len(monster_spots) * sea_monters)
