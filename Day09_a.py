
numbers = []

# Read in stuff
with open("./files/input_09.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(int(line[:-1]))


index = 25
while True:
    options = numbers[index-25:index]
    check = False
    for i, o_1 in enumerate(options):
        for j, o_2 in enumerate(options):
            if o_1 + o_2 == numbers[index] and i != j:
                check = True
                break
        if check:
            break
    if not check:
        break
    index += 1

print(numbers[index])