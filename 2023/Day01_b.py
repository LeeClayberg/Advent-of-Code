
numbers = {'one': '1', 'two': '2','three': '3','four': '4','five': '5','six': '6','seven': '7','eight': '8','nine': '9'}

# Read in stuff
with open("files/day01.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    total = 0
    for line in lines:
        a, b = None, None
        for i in range(0, len(line)):
            if a is None:
                sub_line = line[:i]
                for number in numbers.keys():
                    if number in sub_line:
                        a = numbers[number]
                        break
            if a is None:
                if line[i].isnumeric():
                    a = line[i]
            if b is None:
                sub_line = line[-(i+1):]
                for number in numbers.keys():
                    if number in sub_line:
                        b = numbers[number]
                        break
            if b is None:
                if line[-(i + 1)].isnumeric():
                    b = line[-(i + 1)]
            if a is not None and b is not None:
                break
        c = int(a + b)
        total += c
    print(total)


