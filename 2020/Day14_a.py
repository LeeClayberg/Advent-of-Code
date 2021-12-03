import re

lines = []

# Read in stuff
with open("files/input_14.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

mem = dict()
mask = ""
for line in lines:
    split = re.split('\[|\]| ', line)
    if split[0] == 'mask':
        mask = split[2]
    elif split[0] == 'mem':
        binary_form = "{0:36b}".format(int(split[4])).replace(" ", "0")
        new_form = ""
        for i, val in enumerate(binary_form):
            if mask[i] == 'X':
                new_form += val
            else:
                new_form += mask[i]
        mem[split[1]] = int(new_form, 2)
print(sum(mem.values()))
