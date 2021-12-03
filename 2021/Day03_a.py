
counts = [0 for _ in range(12)]
# Read in stuff
with open("files/input_03.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        for i, c in enumerate(line[:-1]):
            if c == '1':
                counts[i] += 1
            else:
                counts[i] -= 1

new_binary = int(''.join(list(map(lambda x: "1" if int(x) > 0 else "0", counts))), 2)
second_binary = int(''.join(list(map(lambda x: "0" if int(x) > 0 else "1", counts))), 2)
print(new_binary * second_binary)

