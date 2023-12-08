
with open("files/day08.txt", "r") as file_stream:
    lines = file_stream.readlines()

    instructions = lines[0]
    network = {line.split(' = ')[0]: line.split(' = ')[1][1:-2].split(', ') for line in lines[2:]}

    node = 'AAA'
    index = 0
    while node != 'ZZZ':
        step = instructions[index % (len(instructions)-1)]
        node = network[node][0 if step == 'L' else 1]
        print(node)
        index += 1
    print(index)

