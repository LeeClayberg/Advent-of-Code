
# Read in stuff
with open("files/day23.txt", "r") as file_stream:
    # Setup
    connections = [line[:-1] for line in file_stream.readlines()]

    graph = {}
    for connection in connections:
        c1, c2 = connection.split('-')
        if c1 not in graph:
            graph[c1] = set()
        graph[c1].add(c2)
        if c2 not in graph:
            graph[c2] = set()
        graph[c2].add(c1)

    groups = set()
    for start in graph.keys():
        for middle in graph[start]:
            for end in graph[middle]:
                if end in graph[start] and start < middle < end:
                    group = (start, middle, end)
                    groups.add(group)

    while len(groups) > 1:
        new_groups = set()
        for group in groups:
            shared = graph[group[0]]
            for c in group[1:]:
                shared = shared.intersection(graph[c])
            for c in shared:
                if c > group[-1]:
                    new_groups.add((*group, c))
        groups = new_groups
    print(','.join(groups.pop()))








