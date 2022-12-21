import copy

sequence = []
with open("files/input_20.txt", "r") as file_stream:
    counter = 0
    while True:
        line = file_stream.readline()
        if not line:
            break
        sequence.append((int(line[:-1]), counter))
        counter += 1

current = copy.copy(sequence)
zero = next(c for c in current if c[0] == 0)

# print([c[0] for c in current])
for num in sequence:
    if num[0] != 0:
        idx = current.index(num)
        current.remove(num)

        new_idx = (idx + num[0])
        if new_idx < 0:
            new_idx = len(sequence) - abs(new_idx) - 1
        elif new_idx > len(sequence):
            new_idx = new_idx % len(sequence)
        current.insert(new_idx, num)
        # print([c[0] for c in current])

zero_idx = current.index(zero)
total = 0
for amount in [1000, 2000, 3000]:
    new_idx = (zero_idx + amount) % len(current)
    total += current[new_idx][0]
print(total)
