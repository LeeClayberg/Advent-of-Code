
# Read in stuff
with open("files/day25.txt", "r") as file_stream:
    # Setup
    locks_keys = file_stream.read()[:-1].split('\n\n')

    locks, keys = [], []
    for locks_pin in locks_keys:
        rows = locks_pin.split('\n')
        counts = [sum([1 for row in rows if row[i] == '#']) - 1 for i in range(len(rows[0]))]
        if locks_pin[0] == '#':
            locks.append(counts)
        else:
            keys.append(counts)

    total = 0
    for lock in locks:
        for key in keys:
            if all(k <= 5 - l for l, k in zip(lock, key)):
                total += 1
    print(total)
