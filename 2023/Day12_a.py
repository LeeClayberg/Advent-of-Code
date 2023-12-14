import re

with open("files/day12.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

total = 0
for line in lines:
    record, counts = line.split(' ')
    counts = [int(a) for a in counts.split(',')]

    record = list(record)
    spots = record.count('?')
    for a in range(0, pow(2, spots)):
        symbols = bin(a)[2:]
        symbols = ''.join(['0' for _ in range(0, spots-len(symbols))]) + symbols
        symbols = symbols.replace('0', '.').replace('1', '#')

        new_record = record.copy()
        symbol_idx = 0
        for b in range(0, len(new_record)):
            if new_record[b] == '?':
                new_record[b] = symbols[symbol_idx]
                symbol_idx += 1

        new_record = ''.join(new_record)
        new_record = re.sub('[.]+', '.', new_record)
        parts = [len(part) for part in new_record.split('.') if len(part) > 0]
        if parts == counts:
            total += 1
print(total)