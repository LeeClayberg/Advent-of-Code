import re
# Read in stuff
with open("files/day03.txt", "r") as file_stream:
    data = file_stream.read()

    matches = re.findall(r'mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)', data)

    total = 0
    enabled = True
    for match in matches:
        if match[:3] == "mul" and enabled:
            num1, num2 = match[4:-1].split(',')
            total += int(num1) * int(num2)
        elif match[:3] == "do(":
            enabled = True
        elif match[:3] == "don":
            enabled = False
    print(total)
