
values = []
# Read in stuff
with open("files/input_08.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        signals, output = line.split(" | ")
        values.append((signals.split(), output.split()))

count = 0
for signals, output in values:
    decoded = dict()
    for signal in signals:
        if len(signal) == 2:
            decoded[1] = ''.join(sorted(signal))
        elif len(signal) == 3:
            decoded[7] = ''.join(sorted(signal))
        elif len(signal) == 4:
            decoded[4] = ''.join(sorted(signal))
        elif len(signal) == 7:
            decoded[8] = ''.join(sorted(signal))
    for signal in signals:
        if len(signal) == 5:
            if len(set(decoded[7]).difference(set(signal))) == 0:
                decoded[3] = ''.join(sorted(signal))
            else:
                if len(set(decoded[4]).difference(set(signal))) == 1:
                    decoded[5] = ''.join(sorted(signal))
                else:
                    decoded[2] = ''.join(sorted(signal))
        elif len(signal) == 6:
            if len(set(decoded[4]).difference(set(signal))) == 0:
                decoded[9] = ''.join(sorted(signal))
            else:
                if len(set(decoded[7]).difference(set(signal))) == 0:
                    decoded[0] = ''.join(sorted(signal))
                else:
                    decoded[6] = ''.join(sorted(signal))
    flipped = dict([(value, key) for key, value in decoded.items()])
    count += int(''.join(list(map(lambda x: str(flipped[''.join(sorted(x))]), output))))
print(count)
