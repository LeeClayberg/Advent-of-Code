
# Read in stuff
with open("files/day09.txt", "r") as file_stream:
    lines = file_stream.read()
    line = lines[:-1]

    expanded = []
    id_num = 0
    is_block = True
    for block in line:
        part = str(id_num) if is_block else '.'
        expanded += [part for _ in range(0, int(block))]
        id_num += (1 if is_block else 0)
        is_block = not is_block

    start, end = 0, len(expanded) - 1
    while start < end:
        if expanded[start] != '.':
            start += 1
            continue
        if expanded[end] == '.':
            end -= 1
            continue
        expanded[start] = expanded[end]
        expanded[end] = '.'

    total = 0
    for i, num in enumerate(expanded):
        if num == '.':
            break
        total += (i * int(num))
    print(total)