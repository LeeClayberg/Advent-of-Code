
# Read in stuff
with open("files/day01.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]
    commands = [(line[0], int(line[1:])) for line in lines]

    number = 50
    times_zero = 0
    for direction, amount in commands:
        if direction == 'L':
            number = ((number - amount) + 100) % 100
        else:
            number = ((number + amount) + 100) % 100

        if number == 0:
            times_zero += 1
    print(times_zero)

