
# Read in stuff
with open("files/day19.txt", "r") as file_stream:
    # Setup
    patterns, designs = file_stream.read().split('\n\n')
    patterns = sorted(patterns.split(', '), key=(lambda a: -len(a)))
    designs = designs.split('\n')[:-1]

    count = 0
    for design in designs:
        # Create map
        pattern_map = {}
        for pattern in patterns:
            for i in range(0, len(design) - len(pattern)+1):
                if design[i:i+len(pattern)] == pattern:
                    if i not in pattern_map:
                        pattern_map[i] = []
                    pattern_map[i].append(i+len(pattern))
        # Check if path exists
        seen = set()
        queue = [0]
        found = False
        while len(queue) > 0:
            idx = queue.pop(0)
            if idx in seen:
                continue
            seen.add(idx)
            if idx == len(design):
                found = True
                break
            for n in pattern_map.get(idx, []):
                queue.append(n)
        if found:
            count += 1

    print(count)
