
with open("files/day13.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

before = {
    0: [1, None],
    1: [4, None],
    2: [3, None],
    3: [2, 6],
    4: [5, None],
    5: [2, None],
    6: [12, None],
    7: [8, None],
    8: [None, 12],
    9: [3, 4],
    10: [7, 8],
    11: [1, None],
    12: [1, 5],
    13: [8, None],
    14: [8, None],
    15: [1, None],
    16: [8, None],
    17: [None, 9],
    18: [1, None],
    19: [None, 16],
    20: [1, None],
    21: [10, None],
    22: [None, 10],
    23: [4, None],
    24: [None, 14],
    25: [2, None],
    26: [11, None],
    27: [12, None],
    28: [1, 8],
    29: [3, 6],
    30: [8, None],
    31: [None, 5],
    32: [8, None],
    33: [9, None],
    34: [13, None],
    35: [4, 7],
    36: [1, 6],
    37: [None, 7],
    38: [1, None],
    39: [12, None],
    40: [6, None],
    41: [None, 16],
    42: [2, None],
    43: [2, None],
    44: [8, None],
    45: [None, 6],
    46: [12, None],
    47: [12, None],
    48: [5, None],
    49: [1, 3],
    50: [1, None],
    51: [10, None],
    52: [1, None],
    53: [5, 8],
    54: [2, None],
    55: [8, None],
    56: [4, None],
    57: [None, 10],
    58: [1, 3],
    59: [14, None],
    60: [7, None],
    61: [1, 5],
    62: [2, 8],
    63: [6, 8],
    64: [2, 8],
    65: [4, 7],
    66: [1, 5],
    67: [None, 13],
    68: [3, 7],
    69: [6, None],
    70: [16, None],
    71: [None, 8],
    72: [11, None],
    73: [4, 8],
    74: [1, 7],
    75: [None, 11],
    76: [2, None],
    77: [6, None],
    78: [10, None],
    79: [5, None],
    80: [1, None],
    81: [9, None],
    82: [3, 6],
    83: [16, None],
    84: [10, None],
    85: [10, None],
    86: [None, 12],
    87: [14, None],
    88: [2, None],
    89: [1, 8],
    90: [None, 7],
    91: [None, 16],
    92: [5, 6],
    93: [1, 8],
    94: [None, 14],
    95: [8, None],
    96: [3, 4],
    97: [2, 5],
    98: [6, 6],
    99: [1, 3],
}

def differences (a, b):
    d = 0
    for a, b in zip(stack[-1], row):
        if a != b:
            d += 1
    return d

grids = [[]]
for line in lines:
    if line == '':
        grids.append([])
    else:
        grids[-1].append(line)

total = 0
for w, grid in enumerate(grids):
    horizontal_before = before[w][0]
    vertical_before = before[w][1]
    # horizontal
    stack = [grid[0]]
    unstack = []
    reflecting = False
    mirror = None
    smudge_used = False
    i = 1
    while i < len(grid):
        row = grid[i]

        if len(stack) == 0:
            if smudge_used:
                mirror = i // 2
                break
            else:
                stack.extend(unstack)
                i -= len(unstack) - 1
                unstack = []
                reflecting = False
                smudge_used = False
        elif stack[-1] == row:
            if i == len(grid) - 1 and not smudge_used:
                stack.extend(unstack)
                i -= len(unstack) - 1
                unstack = []
                reflecting = False
            else:
                unstack.insert(0, stack.pop())
                if not reflecting:
                    unstack.append(row)
                reflecting = True
        elif not smudge_used and differences(stack[-1], row) == 1:
            unstack.insert(0, stack.pop())
            if not reflecting:
                unstack.append(row)
            smudge_used = True
            reflecting = True
        else:
            if reflecting:
                stack.extend(unstack)
                i -= len(unstack) - 1
                unstack = []
                reflecting = False
                smudge_used = False
            else:
                stack.append(row)
        i += 1

    if smudge_used and reflecting:
        if mirror is None:
            mirror = len(grid) - len(unstack) + 1
        total += 100 * mirror

    t_grid = [''.join([grid[b][a] for b in range(0, len(grid))]) for a in range(0, len(grid[0]))]

    # vertical
    stack = [t_grid[0]]
    unstack = []
    reflecting = False
    mirror2 = None
    smudge_used = False
    i = 1
    while i < len(t_grid):
        row = t_grid[i]

        if len(stack) == 0:
            if smudge_used:
                mirror2 = i // 2
                break
            else:
                stack.extend(unstack)
                i -= len(unstack) - 1
                unstack = []
                reflecting = False
                smudge_used = False
        elif stack[-1] == row:
            if i == len(t_grid) - 1 and not smudge_used:
                stack.extend(unstack)
                i -= len(unstack) - 1
                unstack = []
                reflecting = False
            else:
                unstack.insert(0, stack.pop())
                if not reflecting:
                    unstack.append(row)
                reflecting = True
        elif not smudge_used and differences(stack[-1], row) == 1:
            unstack.insert(0, stack.pop())
            if not reflecting:
                unstack.append(row)
            smudge_used = True
            reflecting = True
        else:
            if reflecting:
                stack.extend(unstack)
                i -= len(unstack) - 1
                unstack = []
                reflecting = False
                smudge_used = False
            else:
                stack.append(row)
        i += 1

    if smudge_used and reflecting:
        if mirror2 is None:
            mirror2 = len(t_grid) - len(unstack) + 1
        total += mirror2

print(total)
