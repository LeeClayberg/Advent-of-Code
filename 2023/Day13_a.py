
with open("files/day13.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

# grids
grids = [[]]
for line in lines:
    if line == '':
        grids.append([])
    else:
        grids[-1].append(line)

total = 0
for w, grid in enumerate(grids):
    # horizontal
    stack = [grid[0]]
    unstack = []
    reflecting = False
    mirror = None
    for i, row in enumerate(grid[1:]):
        row_num = i + 1

        if len(stack) == 0:
            mirror = row_num // 2
            break
        elif stack[-1] == row:
            unstack.append(row)
            unstack.insert(0, stack.pop())
            reflecting = True
        else:
            if reflecting:
                unstack.append(row)
                stack.extend(unstack)
                unstack = []
                reflecting = False
            else:
                stack.append(row)

    if reflecting:
        if mirror is None:
            mirror = (len(grid) - len(stack)) // 2 + len(stack)
        total += 100 * mirror

    t_grid = [''.join([grid[b][a] for b in range(0, len(grid))]) for a in range(0, len(grid[0]))]

    # vertical
    stack = [t_grid[0]]
    unstack = []
    reflecting = False
    mirror2 = None
    for i, row in enumerate(t_grid[1:]):
        row_num = i + 1

        if len(stack) == 0:
            mirror = row_num // 2
            break
        elif stack[-1] == row:
            unstack.append(row)
            unstack.insert(0, stack.pop())
            reflecting = True
        else:
            if reflecting:
                unstack.append(row)
                stack.extend(unstack)
                unstack = []
                reflecting = False
            else:
                stack.append(row)

    if reflecting:
        if mirror2 is None:
            mirror2 = (len(t_grid) - len(stack)) // 2 + len(stack)
        total += mirror2

    print(f'{w}: [{mirror}, {mirror2}],')
print(total)
