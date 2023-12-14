import time

with open("files/day14.txt", "r") as file_stream:
    lines = file_stream.readlines()
    grid = [line[:-1] for line in lines]

    rounded = []
    cubed_h = {}
    cubed_v = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O':
                rounded.append((x, y))
            elif cell == '#':
                if y not in cubed_h:
                    cubed_h[y] = []
                cubed_h[y].append(x)
                if x not in cubed_v:
                    cubed_v[x] = []
                cubed_v[x].append(y)

    def print_grid(spots):
        grid = [['.' for _ in lines] for _ in lines]
        for y, xs in cubed_h.items():
            for x in xs:
                grid[y][x] = '#'
        for x, y in spots:
            grid[y][x] = 'O'
        for row in grid:
            print(''.join(row))

    # cycle
    seen = {}
    cycle = 0
    while cycle < 172: # changed to match output
        for dir_x, dir_y in [(True, True), (False, True), (True, False), (False, False)]:
            amount_stopped = {}
            new_rounded = []
            for rock in rounded:
                x, y = rock

                if dir_x:
                    new_y = 0 if dir_y else (len(grid) - 1)
                    if x in cubed_v:
                        if dir_y:
                            for option in cubed_v[x]:
                                if y < option:
                                    break
                                else:
                                    new_y = option + 1
                        else:
                            for option in reversed(cubed_v[x]):
                                if y > option:
                                    break
                                else:
                                    new_y = option - 1

                    if x not in amount_stopped:
                        amount_stopped[x] = {}
                    if new_y not in amount_stopped[x]:
                        amount_stopped[x][new_y] = 0
                    else:
                        amount_stopped[x][new_y] += 1 if dir_y else -1

                    new_y += amount_stopped[x][new_y]
                    new_rounded.append((x, new_y))
                else:
                    new_x = 0 if dir_y else (len(grid) - 1)
                    if y in cubed_h:
                        if dir_y:
                            for option in cubed_h[y]:
                                if x < option:
                                    break
                                else:
                                    new_x = option + 1
                        else:
                            for option in reversed(cubed_h[y]):
                                if x > option:
                                    break
                                else:
                                    new_x = option - 1

                    if y not in amount_stopped:
                        amount_stopped[y] = {}
                    if new_x not in amount_stopped[y]:
                        amount_stopped[y][new_x] = 0
                    else:
                        amount_stopped[y][new_x] += 1 if dir_y else -1

                    new_x += amount_stopped[y][new_x]
                    new_rounded.append((new_x, y))

            rounded = new_rounded

        key = str(set(rounded))
        if key in seen:
            print('current:', cycle)
            print('last seen:', seen[key])
            print('starting at', seen[key], 'every', cycle - seen[key])
            print('or after', (1000000000 - seen[key]) % (cycle - seen[key]) + seen[key], 'cycles')
            break
        seen[key] = cycle
        cycle += 1

    total = 0
    for rock in rounded:
        total += len(grid) - rock[1]
    print(total)