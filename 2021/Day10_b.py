from functools import reduce

lines = []
# Read in stuff
with open("files/input_10.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

scores = []
for line in lines:
    stack = []
    check = True
    for char in line:
        try:
            i = [")", "]", "}", ">"].index(char)
            if ["(", "[", "{", "<"].index(stack[-1]) == i:
                stack = stack[:-1]
            else:
                check = False
                break
        except ValueError:
            stack.append(char)
    if check:
        scores.append(reduce(lambda y, x: y * 5 + ["(", "[", "{", "<"].index(x) + 1, reversed(stack), 0))
print(sorted(scores)[len(scores)//2])
