import re
# Read in stuff
with open("files/day03.txt", "r") as file_stream:
    data = file_stream.read()

    matches = re.findall(r'mul\([0-9]+,[0-9]+\)', data)

    total = 0
    for match in matches:
        num1, num2 = match[4:-1].split(',')
        total += int(num1) * int(num2)
    print(total)
