
# Read in stuff
with open("files/day03.txt", "r") as file_stream:
    lines = file_stream.readlines()
    banks = [[int(battery) for battery in line[:-1]] for line in lines]

    total = 0
    for bank in banks:
        max1, max2 = None, None
        for idx, battery in enumerate(bank):
            if max1 is None:
                max1 = battery
            elif max2 is None:
                max2 = battery
            elif max1 < max2:
                max1 = max2
                max2 = battery
            else:
                max2 = max(max2, battery)
        total += int((str(max1) + str(max2)))
    print(total)
