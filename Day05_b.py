import math

lines = []
# Read in stuff
with open("./files/input_05.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line)

seat_ids = list()
highest_id = 0
lowest_id = 10000
for pass_code in lines:
    row = int(pass_code[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(pass_code[7:10].replace("L", "0").replace("R", "1"), 2)
    seat_ids.append(row * 8 + col)
    highest_id = max(highest_id, row * 8 + col)
    lowest_id = min(lowest_id, row * 8 + col)

for i in range(lowest_id, highest_id+1):
    if i not in seat_ids:
        print(i)
