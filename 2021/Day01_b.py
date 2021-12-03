
numbers = []
# Read in stuff
with open("files/input_01.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(int(line))

numbers2 = []
for i in range(len(numbers)-2):
    numbers2.append(numbers[i]+numbers[i+1]+numbers[i+2])

total = 0
for i in range(1, len(numbers2)):
    if numbers2[i] > numbers2[i-1]:
        total += 1
print(total)
