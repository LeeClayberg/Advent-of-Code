from functools import reduce
import numpy as np

lines = []

# Read in stuff
with open("./files/input_20.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

picture_size = 12

pieces = dict()
current_tile = []
current_id = ""
for line in lines:
    if line[:4] == "Tile":
        current_id = line[5:9]
    elif line == "":
        top = current_tile[0]
        bottom = current_tile[-1]
        left = ''.join(list(map(lambda x: x[0], current_tile)))
        right = ''.join(list(map(lambda x: x[-1], current_tile)))
        pieces[current_id] = {'top': top, 'bottom': bottom, 'left': left, 'right': right}
        current_tile = []
    else:
        current_tile.append(line)

same_edge_counts = dict()
for key in pieces.keys():
    key_list = list(pieces.keys())
    key_list.remove(key)
    counter_matches = 0
    for check_key in key_list:
        all_piece_sides = list(pieces[key].values())
        check_piece_sides = list(pieces[check_key].values()) + list(map(lambda x: x[::-1], list(pieces[check_key].values())))
        has_match = len(set(all_piece_sides).intersection(set(check_piece_sides))) > 0
        if has_match:
            counter_matches += 1
    same_edge_counts[key] = {"cm": counter_matches, "id": key}
corners = list(filter(lambda x: x["cm"] == 2, same_edge_counts.values()))
corner_ids = list(map(lambda x: int(x["id"]), corners))
total = reduce((lambda x, y: x * y), corner_ids)
print(total)