
directions = []

# Read in stuff
with open("./files/input_12.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        directions.append({'action': line[:1], 'amount': int(line[1:-1])})

current_position = (0, 0)
way_point = (10, 1)
for dir in directions:
    if dir['action'] == 'N':
        way_point = tuple(map(sum, zip(way_point, (0, dir['amount']))))
    elif dir['action'] == 'E':
        way_point = tuple(map(sum, zip(way_point, (dir['amount'], 0))))
    elif dir['action'] == 'S':
        way_point = tuple(map(sum, zip(way_point, (0, -dir['amount']))))
    elif dir['action'] == 'W':
        way_point = tuple(map(sum, zip(way_point, (-dir['amount'], 0))))
    elif dir['action'] == 'R':
        amount_of_times = int(dir['amount'] / 90)
        for _ in range(amount_of_times):
            way_point = (way_point[1], -way_point[0])
    elif dir['action'] == 'L':
        amount_of_times = int(dir['amount'] / 90)
        for _ in range(amount_of_times):
            way_point = (-way_point[1], way_point[0])
    elif dir['action'] == 'F':
        for _ in range(dir['amount']):
            current_position = tuple(map(sum, zip(current_position, way_point)))
print(abs(current_position[0]) + abs(current_position[1]))
