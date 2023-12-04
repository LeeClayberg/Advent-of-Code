with open("files/day04.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

cards = {}
for line in lines:
    left, right = line.split(': ')
    card = int(left.split(' ')[-1])
    winning, mine = right.split(' | ')
    winning = winning.replace('  ', ' ').split(' ')
    mine = mine.replace('  ', ' ').split(' ')
    count = 0
    for num in mine:
        if num != '' and num in winning:
            count += 1
    for a in range(1, count+1):
        if card + a not in cards:
            cards[card + a] = 1
        cards[card + a] += cards[card] if card in cards else 1
total = 0
for line_num in range(1, len(lines)+1):
    if line_num in cards:
        total += cards[line_num]
    else:
        total += 1
print(total)