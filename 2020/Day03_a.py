
lines = []
# Read in stuff
with open("files/input_03.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line)

slope = (3, 1)
count = 0
index = 0
for level in range(0, len(lines), slope[1]):
    if lines[level][index] == "#":
        count += 1
    index = (index + slope[0]) % (len(lines[0]) - 1)
print(f"{count}")
