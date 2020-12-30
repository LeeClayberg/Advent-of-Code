
numbers = []
# Read in stuff
with open("./files/input_01.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(int(line))

for num1 in numbers:
    for num2 in numbers:
        for num3 in numbers:
            if num1 + num2 + num3 == 2020:
                print(f"{num1*num2*num3}")
                exit(0)
