
lines = []

# Read in stuff
with open("./files/input_13.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

earliest = int(lines[0])
ids = lines[1].split(',')

current_shortest_wait = 100000
bus_id = 0
for i in range(0, len(ids)):
    if ids[i] != 'x':
        amount_until = (int(earliest / int(ids[i])) + 1) * int(ids[i]) - earliest
        if amount_until < current_shortest_wait:
            current_shortest_wait = amount_until
            bus_id = int(ids[i])

print(bus_id * current_shortest_wait)


