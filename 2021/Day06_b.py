
# Read in stuff
with open("files/input_06.txt", "r") as file_stream:
    numbers = list(map(lambda x: int(x), file_stream.readline().split(",")))

    count_each_day = dict()
    for num in numbers:
        if num not in count_each_day.keys():
            count_each_day[num] = 0
        count_each_day[num] += 1
    print(count_each_day)

    total = len(numbers)
    for i in range(256):
        if i in count_each_day.keys():
            total += count_each_day[i]
            if (i + 7) not in count_each_day.keys():
                count_each_day[i + 7] = 0
            count_each_day[i + 7] += count_each_day[i]
            if (i + 9) not in count_each_day.keys():
                count_each_day[i + 9] = 0
            count_each_day[i + 9] += count_each_day[i]
            del count_each_day[i]
    print(total)
