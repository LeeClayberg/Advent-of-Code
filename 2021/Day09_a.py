
numbers = []
# Read in stuff
with open("files/input_09.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(list(map(lambda x: int(x), line[:-1])))

total = 0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        check = True
        if i > 0:
            check &= (numbers[i][j] < numbers[i-1][j])
        if j > 0:
            check &= (numbers[i][j] < numbers[i][j-1])
        if i < len(numbers) - 1:
            check &= (numbers[i][j] < numbers[i+1][j])
        if j < len(numbers[i]) - 1:
            check &= (numbers[i][j] < numbers[i][j+1])
        if check:
            total += numbers[i][j] + 1
print(total)