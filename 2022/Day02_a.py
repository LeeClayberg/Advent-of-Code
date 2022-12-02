
# Read in stuff
current_total = 0
compare = {"A": "X", "B": "Y", "C": "Z"}
win = {"X": "Z", "Y": "X", "Z": "Y"}
points = {"X": 1, "Y": 2, "Z": 3}
with open("files/input_02.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        a, b = line[:-1].split(" ")
        current_total += points[b]
        if compare[a] == win[b]:
            current_total += 6
        elif compare[a] == b:
            current_total += 3
        else:
            current_total += 0

print(current_total)
