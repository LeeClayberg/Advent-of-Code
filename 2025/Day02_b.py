
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
            for size in range(1, length+1):
                if len(str_i) % size != 0:
                    continue
                test = str_i[:size]
                check = True
                for idx in range(1, len(str_i) // size):
                    if test != str_i[idx*size:(idx+1)*size]:
                        check = False
                        break
                if check:
                    total += identifier
                    break
    print(total)