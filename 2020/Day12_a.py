
directions = []

# Read in stuff
with open("files/input_12.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        directions.append({'action': line[:1], 'amount': int(line[1:-1])})

facing_degrees = 0
current_position = (0, 0)
for dir in directions:
    if dir['action'] == 'N':
        current_position = tuple(map(sum, zip(current_position, (0, dir['amount']))))
    elif dir['action'] == 'E':
        current_position = tuple(map(sum, zip(current_position, (dir['amount'], 0))))
    elif dir['action'] == 'S':
        current_position = tuple(map(sum, zip(current_position, (0, -dir['amount']))))
    elif dir['action'] == 'W':
        current_position = tuple(map(sum, zip(current_position, (-dir['amount'], 0))))
    elif dir['action'] == 'R':
        facing_degrees = (facing_degrees - dir['amount']) % 360
    elif dir['action'] == 'L':
        facing_degrees = (facing_degrees + dir['amount']) % 360
    elif dir['action'] == 'F':
        if facing_degrees == 0:
            current_position = tuple(map(sum, zip(current_position, (dir['amount'], 0))))
        elif facing_degrees == 90:
            current_position = tuple(map(sum, zip(current_position, (0, dir['amount']))))
        elif facing_degrees == 180:
            current_position = tuple(map(sum, zip(current_position, (-dir['amount'], 0))))
        elif facing_degrees == 270:
            current_position = tuple(map(sum, zip(current_position, (0, -dir['amount']))))
print(abs(current_position[0]) + abs(current_position[1]))
