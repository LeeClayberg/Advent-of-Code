
connections = dict()

# Read in stuff
with open("files/input_12.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        a, b = line[:-1].split("-")
        if a not in connections.keys():
            connections[a] = []
        connections[a].append(b)
        if b not in connections.keys():
            connections[b] = []
        connections[b].append(a)

small_caves = list(filter(lambda c: c.islower() and c != "start" and c != "end", connections.keys()))

all_paths = set()
for twice in small_caves:
    total = 0
    paths_queue = [["start"]]
    while len(paths_queue) > 0:
        path = paths_queue.pop(0)
        last_cave = path[-1]
        for connection in connections[last_cave]:
            if connection.islower():
                if twice == connection:
                    if path.count(connection) >= 2:
                        continue
                else:
                    if connection in path:
                        continue
            if connection == "start":
                continue
            if connection == "end":
                all_paths.add(','.join(path[1:]))
                continue
            path_copy = path.copy()
            path_copy.append(connection)
            paths_queue.append(path_copy)
print(len(all_paths))
