
# Read in stuff
current_total = 0
with open("files/input_03.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        line2 = file_stream.readline()
        line3 = file_stream.readline()
        first = set(line[:-1])
        second = set(line2[:-1])
        third = set(line3[:-1])
        common = list(first.intersection(second).intersection(third))[0]
        if common == str(common).upper():
            current_total += ord(common)-38
        else:
            current_total += ord(common)-96
    print(current_total)
