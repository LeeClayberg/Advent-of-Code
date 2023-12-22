
with open("files/day12.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

for l, line in enumerate(lines):
    record, groups = line.split(' ')
    groups = [int(a) for a in groups.split(',')]

    print(record)

