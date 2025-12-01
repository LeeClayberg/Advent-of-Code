
# Read in stuff
with open("files/day01.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]
    commands = [(line[0], int(line[1:])) for line in lines]

    number = 50
    times_zero = 0
    for direction, amount in commands:
        times_zero += amount // 100
        new_amount = amount % 100
        if direction == 'L':
            if number != 0 and number - new_amount <= 0:
                times_zero += 1
            number = ((number - new_amount) + 100) % 100
        else:
            if number != 0 and number + new_amount >= 100:
                times_zero += 1
            number = ((number + new_amount) + 100) % 100
    print(times_zero)

