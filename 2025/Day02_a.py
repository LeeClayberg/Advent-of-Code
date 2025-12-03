
# Read in stuff
with open("files/day02.txt", "r") as file_stream:
    line = file_stream.read()
    ranges = [value.split('-') for value in line.split(',')]

    total = 0
    for start, end in ranges:
        start_i, end_i = int(start), int(end)
        for identifier in range(start_i, end_i+1):
            str_i = str(identifier)
            length = len(str_i) // 2
            front, back = str_i[:length], str_i[length:]
            if front == back:
                total += identifier
    print(total)