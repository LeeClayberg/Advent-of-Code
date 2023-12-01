
# Read in stuff
with open("files/day01.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    total = 0
    for line in lines:
        line_back = list(reversed(line))
        a,b = None, None
        for i in range(0, len(line)):
            if a is None and line[i].isnumeric():
                a = line[i]
            if b is None and line_back[i].isnumeric():
                b = line_back[i]
            if a is not None and b is not None:
                break
        c = int(a + b)
        total += c
    print(total)

