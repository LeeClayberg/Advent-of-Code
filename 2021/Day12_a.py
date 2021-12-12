
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

total = 0
paths_queue = [["start"]]
while len(paths_queue) > 0:
    path = paths_queue.pop(0)
    last_cave = path[-1]
    for connection in connections[last_cave]:
        if connection.islower() and connection in path:
            continue
        if connection == "end":
            total += 1
            continue
        path_copy = path.copy()
        path_copy.append(connection)
        paths_queue.append(path_copy)
print(total)
