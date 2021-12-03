
numbers = []
# Read in stuff
with open("files/input_02.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        operation, value = line.split()
        if operation == "forward":
            numbers.append((int(value), 0))
        elif operation == "down":
            numbers.append((0, int(value)))
        elif operation == "up":
            numbers.append((0, -int(value)))

total_h, total_d = 0, 0
for pair in numbers:
    total_h += pair[0]
    total_d += pair[1]
print(total_h * total_d)
