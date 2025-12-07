import re
import collections

# Read in stuff
with open("files/day06.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    num_groups = [[]]
    ops = re.split('\s+', lines[-1])

    idx = 0
    while idx < len(lines[0]):
        d1, d2, d3, d4 = lines[0][idx], lines[1][idx], lines[2][idx], lines[3][idx]
        if d1 == d2 == d3 == d4 == ' ':
            num_groups.append([])
        else:
            num_groups[-1].append(int((d1 + d2 + d3 + d4).replace(' ', '')))
        idx += 1

    total = 0
    for g, group in enumerate(num_groups):
        sub_total = None
        for num in group:
            if ops[g] == '*':
                if sub_total is None:
                    sub_total = num
                else:
                    sub_total *= num
            else:
                if sub_total is None:
                    sub_total = num
                else:
                    sub_total += num
        total += sub_total
    print(total)



