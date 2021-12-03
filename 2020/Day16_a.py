import re

lines = []

# Read in stuff
with open("files/input_16.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

fields = dict()
for line in lines[:20]:
    split = re.split(': |-| or ', line)
    fields[split[0]] = list(range(int(split[1]), int(split[2])+1)) + list(range(int(split[3]), int(split[4])+1))

sum_t = 0
for line in lines[25:]:
    numbers = line.split(',')
    for num in numbers:
        check = False
        for field in fields.values():
            if int(num) in field:
                check = True
                break
        if not check:
            sum_t += int(num)
print(sum_t)
