
# Read in stuff
with open("files/day01.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    left, right = [], []
    for line in lines:
        add_left, add_right = line.split("   ")
        left.append(int(add_left))
        right.append(int(add_right))

    left.sort()
    right.sort()

    total = 0
    for l, r in zip(left, right):
        total += abs(l - r)
    print(total)
