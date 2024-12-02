
# Read in stuff
with open("files/day01.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    left, right = [], {}
    for line in lines:
        add_left, add_right = line.split("   ")
        left.append(int(add_left))
        num = int(add_right)
        if num not in right:
            right[num] = 0
        right[num] += 1

    total = 0
    for l in left:
        if l in right:
            total += l * right[l]
    print(total)


