import re
# Read in stuff
with open("files/day04.txt", "r") as file_stream:
    lines = file_stream.readlines()
    search = [[a for a in line[:-1]] for line in lines]

    # Create map
    total = 0
    points = set()
    for i, row in enumerate(search):
        for j, char in enumerate(row):
            if char != 'X':
                continue
            for a, b in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
                found = True
                sub_points = {(i, j)}
                for s, check in enumerate(['M', 'A', 'S']):
                    new_i, new_j = i + a * (s + 1), j + b * (s + 1)
                    if new_i < 0 or new_i >= len(search) or new_j < 0 or new_j >= len(search[0]):
                        found = False
                        break
                    if search[new_i][new_j] != check:
                        found = False
                        break
                    sub_points.add((new_i, new_j))
                if found:
                    total += 1
                    points = points.union(sub_points)
    print(total)


    # full = ""
    # for i, row in enumerate(search):
    #     part = ""
    #     for j, char in enumerate(row):
    #         if (i, j) in points:
    #             part += f"{char} "
    #         else:
    #             part += f". "
    #     full += part + "\n"
    # print(full)