
values = {'A': 23, 'K': 22, 'Q': 21, 'J': 20, 'T': 19, '9': 18, '8': 17, '7': 16, '6': 15, '5': 14, '4': 13, '3': 12, '2': 11}

with open("files/day07.txt", "r") as file_stream:
    lines = file_stream.readlines()

    hands = [(line.split()[0], int(line.split()[1])) for line in lines]
    hands_ext = []
    for hand, bid in hands:
        counts = dict()
        for card in hand:
            if card not in counts:
                counts[card] = 0
            counts[card] += 1
        card_count = len(counts)

        if card_count == 1:
            key = 'g'
        elif card_count == 2:
            if 4 in counts.values():
                key = 'f'
            else:
                key = 'e'
        elif card_count == 3:
            if 3 in counts.values():
                key = 'd'
            else:
                key = 'c'
        elif card_count == 4:
            key = 'b'
        else:
            key = 'a'

        for card in hand:
            key += str(values[card])

        hands_ext.append((hand, bid, key))
    hands_ext.sort(key=(lambda x: x[2]))

    total = 0
    for i, value in enumerate(hands_ext):
        total += (i+1) * value[1]
    print(total)