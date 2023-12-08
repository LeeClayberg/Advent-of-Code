from math import gcd

with open("files/day08.txt", "r") as file_stream:
    lines = file_stream.readlines()

    instructions = lines[0]
    network = {line.split(' = ')[0]: line.split(' = ')[1][1:-2].split(', ') for line in lines[2:]}

    index = 0
    nodes = [key for key in network.keys() if key[-1] == 'A']

    numbers = []
    for node in nodes:
        index = 0
        while node[-1] != 'Z':
            step = instructions[index % (len(instructions) - 1)]
            node = network[node][0 if step == 'L' else 1]
            index += 1
        numbers.append(index)
    print(numbers)
    # All finishes happened on the same instruction!

    lcm = 1
    for i in numbers:
        lcm = lcm * i // gcd(lcm, i)
    print(lcm)


    # while True:
    #     step = instructions[index % (len(instructions)-1)]
    #     nodes = [network[node][0 if step == 'L' else 1] for node in nodes]
    #     index += 1
    #     if len([node for node in nodes if node[-1] == 'Z']) == len(nodes):
    #         print(index)
    #         break
