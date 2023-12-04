with open("files/day04.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

total = 0
for line in lines:
    left, right = line.split(': ')
    winning, mine = right.split(' | ')
    winning = winning.replace('  ', ' ').split(' ')
    mine = mine.replace('  ', ' ').split(' ')
    count = 0
    for num in mine:
        if num != '' and num in winning:
            if count == 0:
                count = 1
            else:
                count *= 2
    total += count
print(total)

