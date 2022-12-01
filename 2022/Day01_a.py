
# Read in stuff
current_max = 0
current_sum = 0
with open("files/input_01.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        if line == '\n':
            current_max = max(current_max, current_sum)
            current_sum = 0
        else:
            current_sum += int(line)
print(current_max)
