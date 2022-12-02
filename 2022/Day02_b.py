
# Read in stuff
current_total = 0
compare = {"A": "X", "B": "Y", "C": "Z"}
win = {"X": "Z", "Y": "X", "Z": "Y"}
lose = {v: k for k, v in win.items()}
print(lose)
points = {"X": 1, "Y": 2, "Z": 3}
with open("files/input_02.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        a, b = line[:-1].split(" ")
        if b == 'X':
            current_total += points[win[compare[a]]]
        elif b == 'Y':
            current_total += 3
            current_total += points[compare[a]]
        else:
            current_total += 6
            current_total += points[lose[compare[a]]]

print(current_total)
