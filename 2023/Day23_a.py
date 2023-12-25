import networkx as nx

with open("files/day23.txt", "r") as file_stream:
    grid = file_stream.readlines()
    grid = [line[:-1] for line in grid]

    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

    G = nx.DiGraph()

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            cell = grid[y][x]
            if cell == '#':
                continue
            keys = directions.keys()
            if cell == '^':
                keys = ['U']
            elif cell == '<':
                keys = ['L']
            elif cell == '>':
                keys = ['R']
            elif cell == 'v':
                keys = ['D']

            for dir_pros in keys:
                change = directions[dir_pros]
                new_pos = (x+change[0], y+change[1])
                if 0 > new_pos[0] or new_pos[0] >= len(grid[0]) or 0 > new_pos[1] or new_pos[1] >= len(grid):
                    continue
                if grid[new_pos[1]][new_pos[0]] == '#':
                    continue
                G.add_edge((x, y), (new_pos[0], new_pos[1]))

    start = (grid[0].index('.'), 0)
    end = (grid[-1].index('.'), len(grid)-1)

    d = nx.all_simple_paths(G, start, end)
    max_path = max(d, key=(lambda path: len(path)))
    print(len(max_path)-1)