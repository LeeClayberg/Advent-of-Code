
lines = []

# Read in stuff
with open("files/input_06.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            lines.append('')
            break
        lines.append(line[:-1])

total = 0
letters = set("qwertyuiopasdfghjklzxcvbnm")
for answer in lines:
    if answer == '':
        total += len(letters)
        letters = set("qwertyuiopasdfghjklzxcvbnm")
    else:
        letters = letters.intersection(set(answer))
print(total)
