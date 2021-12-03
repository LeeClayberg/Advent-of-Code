
lines = []
# Read in stuff
with open("files/input_02.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line)

total_count = 0
for line in lines:
    parts = line.split(" ")
    lower_bound = int(parts[0].split("-")[0])
    upper_bound = int(parts[0].split("-")[1])
    letter = parts[1][0]
    if lower_bound <= len(list(filter(lambda x: x == letter, parts[2]))) <= upper_bound:
        total_count += 1
print(total_count)
