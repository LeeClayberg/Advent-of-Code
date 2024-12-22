
# Read in stuff
with open("files/day17.txt", "r") as file_stream:
    # Setup
    registers, program = file_stream.read().split('\n\n')
    a, b, c = [int(register.split(' ')[-1]) for register in registers.split('\n')]
    program = [int(p) for p in program[:-1].split(' ')[-1].split(',')]

    sa = 0
    while True:
        a, b, c = sa, 0, 0
        output = []
        while a > 0:
            b = a % 8
            b = b ^ 6
            c = a // pow(2, b)
            b = b ^ c
            b = b ^ 4
            output.append(b % 8)
            a = a // 8
        if output == program:
            print(sa)
            exit()
        sa += 1

    # while len(output) > 0:
    #     a *= 8
    #     b = x * 8 + output.pop()
    #     b = b ^ 4
    #     b = b ^ c
    #     a = c * pow(2, b)
    #     b = b ^ 6
    #     a = y * 8 + b
    #     print(a, b, c)
    # print(a, b, c)

# 2,4, -> b = a % 8
# 1,6, -> b = b ^ 6
# 7,5, -> c = a // pow(2, b)
# 4,6, -> b = b ^ c
# 1,4, -> b = b ^ 4
# 5,5, -> out = b % 8
# 0,3, -> a = a // 8
# 3,0  -> goes back to start if a is not 0