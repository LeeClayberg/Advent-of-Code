
# Read in stuff
current_total = 0
with open("files/input_03.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        line = line[:-1]
        right = set(line[len(line)//2:])
        left = set(line[:len(line)//2])
        common = list(right.intersection(left))[0]
        if common == str(common).upper():
            current_total += ord(common)-38
        else:
            current_total += ord(common)-96
    print(current_total)
