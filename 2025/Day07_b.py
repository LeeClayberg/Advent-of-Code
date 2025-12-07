
# Read in stuff
with open("files/day07.txt", "r") as file_stream:
    rows = file_stream.readlines()
    rows = [row[:-1] for row in rows]
    rows.append(['^' for _ in range(0, len(rows[0]))]) # Add for reaching end

    first_x = rows[0].find('S')

    tree = {}
    beams = {first_x: [(0, 'center')]}
    for ridx, row in enumerate(rows[1:]):
        new_beams = beams
        for idx, cell in enumerate(row):
            if idx in beams and cell == '^':
                if idx-1 not in beams:
                    new_beams[idx-1] = []
                new_beams[idx-1].append((ridx+1, 'left'))
                if idx+1 not in beams:
                    new_beams[idx+1] = []
                new_beams[idx+1].append((ridx+1, 'right'))
                connected_beams = beams[idx]
                for beam in connected_beams:
                    if beam[1] == 'center':
                        parent_key = (idx, beam[0])
                    if beam[1] == 'left':
                        parent_key = (idx+1, beam[0])
                    if beam[1] == 'right':
                        parent_key = (idx-1, beam[0])
                    key = (idx, ridx+1)
                    if parent_key not in tree:
                        tree[parent_key] = []
                    tree[parent_key].append(key)
                del new_beams[idx]
        beams = new_beams

    cache = {}
    def recurse(point):
        if point in cache:
            return cache[point]
        if point not in tree:
            return 1
        leaves = tree[point]
        if len(leaves) == 0:
            return 1
        else:
            total = 0
            for leaf in leaves:
                total += recurse(leaf)
            cache[point] = total
            return total

    start = (first_x, 0)
    print(recurse(start))