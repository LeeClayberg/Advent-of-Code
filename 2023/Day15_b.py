
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

    boxes = {}
    for step in steps:

        if '=' in step:
            label, operation, focal = step.split('=')[0], '=', step.split('=')[1]
        else:
            label, operation = step[:-1], '-'

        box = hash(label)

        if box not in boxes:
            boxes[box] = {}

        if operation == '-':
            if label in boxes[box]:
                del boxes[box][label]
        else:
            boxes[box][label] = int(focal)

    total = 0
    for b, box in boxes.items():
        for s, focal in enumerate(box.values()):
            total += (int(b)+1) * (s+1) * focal
    print(total)


