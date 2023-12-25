import networkx as nx

with open("files/day23.txt", "r") as file_stream:
    grid = file_stream.readlines()
    grid = [line[:-1] for line in grid]

    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

    start = (grid[0].index('.'), 0)
    end = (grid[-1].index('.'), len(grid)-1)

    queue = [(start, [])]
    paths = []
    while len(queue) > 0:
        node, path = queue.pop()
        x, y = node

        if node == end:
            paths.append(path)

        for dir_pros in directions.keys():
            change = directions[dir_pros]
            new_pos = (x + change[0], y + change[1])
            if new_pos in path:
                continue
            if 0 > new_pos[0] or new_pos[0] >= len(grid[0]) or 0 > new_pos[1] or new_pos[1] >= len(grid):
                continue
            if grid[new_pos[1]][new_pos[0]] == '#':
                continue
            queue.append((new_pos, path + [node]))

    max_path = max(paths, key=(lambda p: len(p)))
    print(len(max_path))
    for i, row in enumerate(grid):
        print(''.join(['O' if (j, i) in max_path else cell for j, cell in enumerate(row)]))