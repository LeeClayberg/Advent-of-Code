
# Read in stuff
with open("files/day17.txt", "r") as file_stream:
    # Setup
    registers, program = file_stream.read().split('\n\n')
    a, b, c = [int(register.split(' ')[-1]) for register in registers.split('\n')]
    program = [int(p) for p in program[:-1].split(' ')[-1].split(',')]


    output = [o for o in program]
    ip = len(program) - 1
    while 0 <= ip:
        operand = program[ip]
        ip -= 1
        opcode = program[ip]
        ip -= 1

        if opcode == 0: # adv
            a = a // pow(2, combo(operand))
        elif opcode == 1: # bxl
            b = b ^ operand
        elif opcode == 2:  # bst
            b = combo(operand) % 8
        elif opcode == 3: # jnz
            if a != 0:
                ip = operand
        elif opcode == 4: # bxc
            b = b ^ c
        elif opcode == 5: # out -
            mod = output.pop()
            if operand == 4:
                a = mod
            elif operand == 5:
                b = mod
            elif operand == 6:
                c = mod
        elif opcode == 6: # bdv
            if operand == 4:
                a = mod
            elif operand == 5:
                b = mod
            elif operand == 6:
                c = mod
            else:

            b = a // pow(2, combo(operand))
        elif opcode == 7: # cdv
            c = a // pow(2, combo(operand))

    print(output)
