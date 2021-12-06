
# Read in stuff
with open("files/input_06.txt", "r") as file_stream:
    numbers = list(map(lambda x: int(x), file_stream.readline().split(",")))

    for _ in range(80):
        for i in range(len(numbers)):
            if numbers[i] == 0:
                numbers[i] = 6
                numbers.append(8)
            else:
                numbers[i] -= 1
    print(len(numbers))
