
numbers = []

# Read in stuff
with open("./files/input_10.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(int(line[:-1]))

numbers.sort()

one_jolt = 1
three_jolt = 1

for i in range(len(numbers) - 1):
    if numbers[i+1] - numbers[i] == 1:
        one_jolt += 1
    elif numbers[i+1] - numbers[i] == 3:
        three_jolt += 1
print(one_jolt * three_jolt)
