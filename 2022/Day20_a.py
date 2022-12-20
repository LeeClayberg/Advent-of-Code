
sequence = []
with open("files/input_20.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        sequence.append(int(line[:-1]))
sequ_idx = [i for i in range(len(sequence))]

idx = 0
while idx < len(sequence):
    sequ_idx[idx] = (sequ_idx[idx] + sequence[idx]) % len(sequence)
    sequ_idx = [a for a in sequ_idx]
    idx += 1

