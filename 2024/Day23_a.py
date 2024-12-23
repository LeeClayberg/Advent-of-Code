
# Read in stuff
with open("files/day23.txt", "r") as file_stream:
    # Setup
    connections = [line[:-1] for line in file_stream.readlines()]

    graph = {}
    for connection in connections:
        c1, c2 = connection.split('-')
        if c1 not in graph:
            graph[c1] = []
        graph[c1].append(c2)
        if c2 not in graph:
            graph[c2] = []
        graph[c2].append(c1)

    groups = set()
    for start in graph.keys():
        for middle in graph[start]:
            for end in graph[middle]:
                if end in graph[start] and start < middle < end:
                    group = (start, middle, end)
                    groups.add(group)

    total = 0
    for c1, c2, c3 in groups:
        if c1[0] == 't' or c2[0] == 't' or c3[0] == 't':
            total += 1
    print(total)
