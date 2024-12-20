
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

        # Count paths
        cache = {}

        def count_poss(key):
            if key == len(design):
                return 1
            total = 0
            for n in pattern_map.get(key, []):
                if n not in cache:
                    cache[n] = count_poss(n)
                total += cache[n]
            return total


        count += count_poss(0)

    print(count)
