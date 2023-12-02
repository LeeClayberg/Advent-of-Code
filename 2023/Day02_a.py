
bag = {'red': 12, 'green': 13, 'blue': 14}

with open("files/day02.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    total = 0
    for line in lines:
        id, sets = line.split(': ')
        id = int(id.split(' ')[1])
        sets = sets.split('; ')

        check = True
        for s in sets:
            groups = s.split(', ')
            for group in groups:
                num, color = group.split(' ')
                if bag[color] < int(num):
                    check = False
                    break
            if not check:
                break
        if check:
            total += id
    print(total)

