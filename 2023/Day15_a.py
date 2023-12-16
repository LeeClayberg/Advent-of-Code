
def hash(step):
    sub_total = 0
    for char in step:
        asc = ord(char)
        sub_total += asc
        sub_total *= 17
        sub_total %= 256
    return sub_total

with open("files/day15.txt", "r") as file_stream:
    line = file_stream.readline()
    line = line[:-1]
    steps = line.split(',')

    total = 0
    for step in steps:
        total += hash(step)
    print(total)