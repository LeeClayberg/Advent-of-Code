values = []

# Read in stuff
cycle = 1
x = 1
check = 20
with open("files/input_10.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        instr = line[:-1]

        cycle += 1
        # Check cycle
        if cycle == check:
            values.append(check * x)
            check += 40
            print(x)
        if instr != 'noop':
            cycle += 1
            x += int(instr.split(' ')[1])
            # Check cycle
            if cycle == check:
                values.append(check * x)
                check += 40
                print(x)
print(sum(values))
