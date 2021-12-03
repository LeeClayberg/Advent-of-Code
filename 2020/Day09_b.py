
numbers = []

# Read in stuff
with open("files/input_09.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(int(line[:-1]))

# answer from part 1
num = 1721308972

numbers = list(filter(lambda x: x < num, numbers))

for size_of_block in range(1, len(numbers)):
    current_start = 0
    check = False
    while current_start + size_of_block < len(numbers) - 1:
        sub_set = numbers[current_start:current_start+size_of_block]
        if sum(sub_set) == num:
            print(f"{min(sub_set) + max(sub_set)}")
            check = True
            break
        current_start += 1
    if check:
        break
