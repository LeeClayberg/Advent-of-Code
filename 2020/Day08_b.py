
lines = []

# Read in stuff
with open("files/input_08.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

index = 0
present = 0
acc = 0
while index != len(lines):
    instructions_read = set()
    index = 0
    acc = 0
    counter = 0
    while index not in instructions_read and index < len(lines):
        instructions_read.add(index)
        parts = lines[index].split(" ")
        oper = parts[0]
        is_pos = '+' in parts[1]
        num = int(parts[1][1:])

        if counter == present:
            if oper == 'nop':
                oper = 'jmp'
            elif oper == 'jmp':
                oper = 'nop'

        if oper == 'acc':
            if is_pos:
                acc += num
                index += 1
            else:
                acc -= num
                index += 1
        elif oper == 'jmp':
            if is_pos:
                index += num
            else:
                index -= num
        elif oper == 'nop':
            index += 1
        if oper == 'nop':
            counter += 1
        elif oper == 'jmp':
            counter += 1
    present += 1
print(acc)
