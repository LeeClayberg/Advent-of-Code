
numbers = []

# Read in stuff
with open("files/input_10.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(int(line[:-1]))


def find_choices_rec(idx, num):
    if num < 3:
        return 1
    choices = 1
    for i in range(2, idx+1):
        for b in range(1, int(num / i) + 1):
            extra = num - b * i
            choices += extra
    return choices


numbers.append(0)
numbers.sort()

total = 1
size = 1
for i in range(1, len(numbers)):
    if numbers[i] - numbers[i-1] == 1:
        size += 1
    elif numbers[i] - numbers[i-1] == 3:
        total *= find_choices_rec(min(3, size-1), size)
        size = 1
total *= find_choices_rec(min(3, size-1), size)
print(total)
