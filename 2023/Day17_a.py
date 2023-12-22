import networkx as nx

with open("files/day17.txt", "r") as file_stream:
    grid = file_stream.readlines()
    grid = [line[:-1] for line in grid]

    directions = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

    G = nx.DiGraph()

    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            for dir_curr in directions.keys():
                for i in range(0, 3):
                    for dir_pros in [key for key in directions.keys() if key != opposite[dir_curr]]:
                        change = directions[dir_pros]
                        new_pos = (x+change[0], y+change[1])
                        if 0 > new_pos[0] or new_pos[0] >= len(grid[0]) or 0 > new_pos[1] or new_pos[1] >= len(grid):
                            continue

                        if i == 2 and dir_curr == dir_pros:
                            continue
                        new_i = 0 if dir_curr != dir_pros else (i + 1)
                        G.add_edge((x, y, dir_curr, i), (new_pos[0], new_pos[1], dir_pros, new_i), weight=int(grid[new_pos[1]][new_pos[0]]))

    G.add_edge((0, 0, 'S', 0), (1, 0, 'R', 0), weight=int(grid[0][1]))
    G.add_edge((0, 0, 'S', 0), (0, 1, 'D', 0), weight=int(grid[1][0]))
    print('graph done')

    end_nodes = [key for key in G.nodes.keys() if key[0] == len(grid[0]) - 1 and key[1] == len(grid) - 1]

    minimum = 10000000000
    for node in end_nodes:
        try:
            d = nx.dijkstra_path_length(G, (0, 0, 'S', 0), node)
            minimum = min(minimum, d)
        except:
            print('No path')
    print(minimum)