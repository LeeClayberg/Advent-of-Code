
values = {'A': 23, 'K': 22, 'Q': 21, 'T': 20, '9': 19, '8': 18, '7': 17, '6': 16, '5': 15, '4': 14, '3': 13, '2': 12, 'J': 11}

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

        if len(counts) > 1:
            count_list = list(counts.items())
            count_list.sort(key=(lambda pair: str(pair[1]) + str(values[pair[0]])), reverse=True)
            if count_list[0][0] != 'J':
                if 'J' in counts:
                    counts[count_list[0][0]] += counts['J']
                    del counts['J']
            else:
                counts[count_list[1][0]] += counts['J']
                del counts['J']

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