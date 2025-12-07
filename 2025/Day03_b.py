
# Read in stuff
with open("files/day03.txt", "r") as file_stream:
    lines = file_stream.readlines()
    banks = [[int(battery) for battery in line[:-1]] for line in lines]

    total = 0
    for bank in banks:
        number_indexes = [i for i in range(len(bank)-12, len(bank))]
        for ii, start_idx in enumerate(range(len(bank)-13, len(bank)-1)):
            max_back = number_indexes[ii-1] if ii > 0 else -1
            for idx in range(start_idx, max_back, -1):
                if bank[number_indexes[ii]] <= bank[idx]:
                    number_indexes[ii] = idx
        total += int(''.join([str(bank[idx]) for idx in number_indexes]))
    print(total)
