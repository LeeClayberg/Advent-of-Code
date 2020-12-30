import math

lines = []
# Read in stuff
with open("./files/input_05.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line)

highest_seat_id = 0
for pass_code in lines:
    row = int(pass_code[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(pass_code[7:10].replace("L", "0").replace("R", "1"), 2)
    highest_seat_id = max(row * 8 + col, highest_seat_id)
print(highest_seat_id)
