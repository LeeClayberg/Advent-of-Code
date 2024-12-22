
# Read in stuff
with open("files/day21.txt", "r") as file_stream:
    # Setup
    codes = file_stream.read().split('\n')

    # Button locations
    numeric_buttons = {'7': (0, 0), '8': (1, 0), '9': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '1': (0, 2), '2': (1, 2), '3': (2, 2), '0': (1, 3), 'A': (2, 3)}
    directional_buttons = {'^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1),}

    # Numeric graph
    positions = numeric_buttons.values()
    numeric_map = {position: [] for position in positions}
    for button in positions:
        x, y = button
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in positions:
                numeric_map[button].append((nx, ny))

    # Directional graph
    positions = directional_buttons.values()
    directional_map = {position: [] for position in positions}
    for button in positions:
        x, y = button
        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) in positions:
                directional_map[button].append((nx, ny))

    # Shortest paths between numeric buttons
    numeric_shortest_paths = {}
    for num1 in numeric_buttons.keys():
        # Add weights based on distance
        start = numeric_buttons[num1]
        weights = {p: [(10000000, None, None)] for p in numeric_map.keys()}
        weights[start] = [(0, None, '')]
        queue = [start]
        while len(queue) > 0:
            p = queue.pop(0)
            x, y = p
            for w, d, s in weights[p]:
                for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    np, nd = (nx, ny), (dx, dy)
                    if np in numeric_map.keys():
                        nw = w + 1
                        if d is not None and (dx, dy) != d:
                            nw += 10
                        if nw <= weights[np][0][0]:
                            options = {(0, -1): '^', (-1, 0): '<', (1, 0): '>', (0, 1): 'v'}
                            if nw < weights[np][0][0]:
                                weights[np] = []
                            weights[np].append((nw, nd, s + options[nd]))
                            queue.append(np)

        # Find paths
        for num2 in numeric_buttons.keys():
            if num1 == num2:
                continue
            key = num1 + num2
            point = numeric_buttons[num2]
            numeric_shortest_paths[key] = list(set([weight[2] for weight in weights[point]]))

    # Shortest paths between directional buttons
    directional_shortest_paths = {}
    for num1 in directional_buttons.keys():
        # Add weights based on distance
        start = directional_buttons[num1]
        weights = {p: [(10000000, None, None)] for p in directional_map.keys()}
        weights[start] = [(0, None, '')]
        queue = [start]
        while len(queue) > 0:
            p = queue.pop(0)
            for w, d, s in weights[p]:
                x, y = p
                for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    np, nd = (nx, ny), (dx, dy)
                    if np in directional_map.keys():
                        nw = w + 1
                        if d is not None and (dx, dy) != d:
                            nw += 10
                        if nw <= weights[np][0][0]:
                            options = {(0, -1): '^', (-1, 0): '<', (1, 0): '>', (0, 1): 'v'}
                            if nw < weights[np][0][0]:
                                weights[np] = []
                            weights[np].append((nw, nd, s + options[nd]))
                            queue.append(np)

        # Find paths
        for num2 in directional_buttons.keys():
            if num1 == num2:
                continue
            key = num1 + num2
            point = directional_buttons[num2]
            directional_shortest_paths[key] = list(set([weight[2] for weight in weights[point]]))

    total = 0
    for code in codes:
        # Robot directional pad #1
        path = 'A' + code
        new_paths = [""]
        for i in range(0, len(path) -1):
            segment = path[i:i+2]
            seg_paths = numeric_shortest_paths[segment]
            if len(seg_paths) == 1:
                new_paths = [new_path + seg_paths[0] + 'A' for new_path in new_paths]
            else:
                new_new_paths = []
                for seg_path in seg_paths:
                    for new_path in new_paths:
                        new_new_paths.append(new_path + seg_path + 'A')
                new_paths = new_new_paths

        # Robot directional pad #2
        outer_paths = []
        for spath in new_paths:
            path = 'A' + spath
            new_paths = [""]
            for i in range(0, len(path) - 1):
                segment = path[i:i + 2]
                if segment in directional_shortest_paths:
                    seg_paths = directional_shortest_paths[segment]
                else:
                    seg_paths = ['']
                if len(seg_paths) == 1:
                    new_paths = [new_path + seg_paths[0] + 'A' for new_path in new_paths]
                else:
                    new_new_paths = []
                    for seg_path in seg_paths:
                        for new_path in new_paths:
                            new_new_paths.append(new_path + seg_path + 'A')
                    new_paths = new_new_paths
            outer_paths += new_paths
        new_paths = outer_paths

        # Personal directional pad
        outer_paths = []
        for spath in new_paths:
            path = 'A' + spath
            new_paths = [""]
            for i in range(0, len(path) - 1):
                segment = path[i:i + 2]
                if segment in directional_shortest_paths:
                    seg_paths = directional_shortest_paths[segment]
                else:
                    seg_paths = ['']
                if len(seg_paths) == 1:
                    new_paths = [new_path + seg_paths[0] + 'A' for new_path in new_paths]
                else:
                    new_new_paths = []
                    for seg_path in seg_paths:
                        for new_path in new_paths:
                            new_new_paths.append(new_path + seg_path + 'A')
                    new_paths = new_new_paths
            outer_paths += new_paths
        new_paths = outer_paths
        shortest_path = min(new_paths, key=lambda p: len(p))
        total += len(shortest_path) * int(code[:-1])
    print(total)
