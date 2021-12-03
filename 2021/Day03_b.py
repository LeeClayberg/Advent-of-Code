
binaries = []
# Read in stuff
with open("files/input_03.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        binaries.append(line[:-1])

binaries_1 = binaries.copy()
i = 0
while True:
    count = 0
    for num in binaries_1:
        if num[i] == '1':
            count += 1
        else:
            count -= 1
    if count >= 0:
        binaries_1 = list(filter(lambda x: x[i] == "1", binaries_1))
    else:
        binaries_1 = list(filter(lambda x: x[i] == "0", binaries_1))
    if len(binaries_1) == 1:
        break
    i += 1

binaries_2 = binaries.copy()
i = 0
while True:
    count = 0
    for num in binaries_2:
        if num[i] == '1':
            count += 1
        else:
            count -= 1
    if count >= 0:
        binaries_2 = list(filter(lambda x: x[i] == "0", binaries_2))
    else:
        binaries_2 = list(filter(lambda x: x[i] == "1", binaries_2))
    if len(binaries_2) == 1:
        break
    i += 1

print(int(binaries_1[0], 2) * int(binaries_2[0], 2))