stacks = [
['R', 'G', 'J', 'B', 'T', 'V', 'Z'],
['J', 'R', 'V', 'L'],
['S', 'Q', 'F'],
['Z', 'H', 'N', 'L', 'F', 'V', 'Q', 'G'],
['R', 'Q', 'T', 'J', 'C', 'S', 'M', 'W'],
['S', 'W', 'T', 'C', 'H', 'F'],
['D', 'Z', 'C', 'V', 'F', 'N', 'J'],
['L', 'G', 'Z', 'D', 'W', 'R', 'F', 'Q'],
['J', 'B', 'W', 'V', 'P'],
]
# Read in stuff
current_total = 0
with open("files/input_05.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        move, count, from_, start, to, end = line.split(" ")
        c, s, e = int(count), int(start), int(end)
        stack = []
        for i in range(c):
            box = stacks[s-1].pop()
            stack.append(box)
        stacks[e - 1] += reversed(stack)

    print(''.join([sub[-1] for sub in stacks]))
