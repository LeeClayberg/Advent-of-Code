
with open("files/day02.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    total = 0
    for line in lines:
        id, sets = line.split(': ')
        id = int(id.split(' ')[1])
        sets = sets.split('; ')

        check = True

        bag = {'red': 0, 'green': 0, 'blue': 0}
        for s in sets:
            groups = s.split(', ')
            for group in groups:
                num, color = group.split(' ')
                if bag[color] < int(num):
                    bag[color] = int(num)
        print(bag)
        power = bag['red'] * bag['green'] * bag['blue']
        print(power)
        total += power
    print(total)

