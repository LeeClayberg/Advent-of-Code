
numbers = []
# Read in stuff
with open("files/input_01.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(int(line))

total = 0
for i in range (1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        total += 1
print(total)
