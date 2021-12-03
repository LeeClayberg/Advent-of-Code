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
        binary_form = "{0:36b}".format(int(split[1])).replace(" ", "0")
        new_form = ""
        for i, val in enumerate(binary_form):
            if mask[i] == '0':
                new_form += val
            else:
                new_form += mask[i]
        for i in range(0, pow(2, new_form.count('X'))):
            format_base = "{0:" + str(new_form.count('X')) + "b}"
            choices = format_base.format(i).replace(" ", "0")
            new_new_form = new_form
            for c in choices:
                new_new_form = new_new_form.replace("X", c, 1)
            mem[int(new_new_form, 2)] = int(split[4])
print(sum(mem.values()))
