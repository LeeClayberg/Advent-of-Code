import re
# Read in stuff
with open("files/day04.txt", "r") as file_stream:
    lines = file_stream.readlines()
    search = [[a for a in line[:-1]] for line in lines]

    # Create map
    total = 0
    for i, row in enumerate(search):
        for j, char in enumerate(row):
            if char != 'A':
                continue
            found = True
            for a, b in [[(-1, -1), (1, 1)], [(1, -1), (-1, 1)]]:
                new_i, new_j = i + a[0], j + a[1]
                new_i2, new_j2 = i + b[0], j + b[1]
                if new_i < 0 or new_i >= len(search) or new_j < 0 or new_j >= len(search[0]):
                    found = False
                    break
                if new_i2 < 0 or new_i2 >= len(search) or new_j2 < 0 or new_j2 >= len(search[0]):
                    found = False
                    break
                if search[new_i][new_j] == 'M' and search[new_i2][new_j2] == 'S':
                    continue
                if search[new_i][new_j] == 'S' and search[new_i2][new_j2] == 'M':
                    continue
                found = False
                break
            if found:
                total += 1
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