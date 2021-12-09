
values = []
# Read in stuff
with open("files/input_08.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        signals, output = line.split(" | ")
        values.append((signals.split(), output.split()))

count = 0
for signals, output in values:
    for digit in output:
        if len(digit) in [2, 3, 4, 7]:
            count += 1
print(count)
