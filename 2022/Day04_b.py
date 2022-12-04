
# Read in stuff
current_total = 0
with open("files/input_04.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        one, two = line.split(",")
        start1, end1 = one.split("-")
        section1 = set(range(int(start1), int(end1) + 1))
        start2, end2 = two.split("-")
        section2 = set(range(int(start2), int(end2) + 1))
        intersection = section1.intersection(section2)
        current_total += 1 if len(intersection) > 0 else 0
    print(current_total)
