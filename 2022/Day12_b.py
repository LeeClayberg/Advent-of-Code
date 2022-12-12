
grid = []
with open("files/input_12.txt", "r") as file_stream:
    while True:
        label = file_stream.readline()
        if not label:
            break
        grid.append([str(a) for a in label[:-1]])


end = None
for a in range(len(grid)):
    for b in range(len(grid[a])):
        if grid[a][b] == 'S':
            grid[a][b] = 'a'
        elif grid[a][b] == 'E':
            end = (a, b)
            grid[a][b] = 'z'

starts = []
graph = dict()
for a, row in enumerate(grid):
    for b, item in enumerate(row):
        if grid[a][b] == 'a':
            starts.append((a, b))
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            s, t = (a + x, b + y)
            if 0 <= s < len(grid) and 0 <= t < len(row) and ord(grid[s][t]) <= ord(grid[a][b]) + 1:
                if (a, b) not in graph.keys():
                    graph[(a, b)] = []
                graph[(a, b)].append((s, t))


shortest_path = 10000
for start in starts:
    path_map = [[-1 for u in row] for row in grid]
    path_map[start[0]][start[1]] = 0

    queue = [start]
    visited = set()
    visited.add(start)
    while len(queue) > 0:
        current = queue.pop(0)
        visited.add(current)
        if current == end:
            shortest_path = min(shortest_path, path_map[current[0]][current[1]])
            break
        for n, m in graph[current]:
            if (n, m) not in visited and (n, m) not in queue:
                queue.append((n, m))
                path_map[n][m] = path_map[current[0]][current[1]] + 1

print(shortest_path)
# print('\n'.join(['\t'.join([str(i) for i in row]) for row in path_map]))