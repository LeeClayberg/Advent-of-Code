# Read in stuff
cycle = 0
x = 1
check = 20
string = "#"
with open("files/input_10.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        instr = line[:-1]

        cycle += 1
        if cycle in range(x-1, x+2):
            string += "#"
        else:
            string += "."
        if cycle == 40:
            string += "\n#"
            cycle = 0
        if instr != 'noop':
            cycle += 1
            x += int(instr.split(' ')[1])
            if cycle in range(x-1, x + 2):
                string += "#"
            else:
                string += "."
            if cycle == 40:
                string += "\n#"
                cycle = 0
print(string[:-1])
