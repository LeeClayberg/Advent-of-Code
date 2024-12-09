
# Read in stuff
with open("files/day09.txt", "r") as file_stream:
    lines = file_stream.read()
    line = lines[:-1]

    coded = []
    id_num = 0
    is_block = True
    for block in line:
        part = str(id_num) if is_block else '.'
        coded.append((part, block))
        id_num += (1 if is_block else 0)
        is_block = not is_block

    start, end = 0, len(coded) - 1
    while 0 < end:
        if start >= end:
            start = 0
            end -= 1
            continue
        if coded[start][0] != '.':
            start += 1
            continue
        if coded[end][0] == '.':
            end -= 1
            continue
        space = int(coded[start][1]) - int(coded[end][1])
        if space < 0:
            start += 1
            continue
        coded[start] = coded[end]
        coded[end] = ('.', coded[end][1])
        coded.insert(start+1, ('.', space))
        start = 0

    expanded = []
    for part, block in coded:
        expanded += [part for _ in range(0, int(block))]

    total = 0
    for i, num in enumerate(expanded):
        if num == '.':
            continue
        total += (i * int(num))
    print(total)