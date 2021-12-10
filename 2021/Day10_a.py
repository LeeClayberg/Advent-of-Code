
lines = []
# Read in stuff
with open("files/input_10.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

total = 0
values = [3, 57, 1197, 25137]
for line in lines:
    stack = []
    for char in line:
        try:
            i = [")", "]", "}", ">"].index(char)
            if ["(", "[", "{", "<"].index(stack[-1]) == i:
                stack = stack[:-1]
            else:
                total += values[i]
                break
        except ValueError:
            stack.append(char)
print(total)
