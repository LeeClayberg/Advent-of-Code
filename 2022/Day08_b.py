matrix = []
# Read in stuff
with open("files/input_08.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        matrix.append([int(x) for x in line[:-1]])

size = len(matrix)

max_count = 0
for a in range(size):
    for b in range(size):
        point = matrix[a][b]
        total = 1

        # right
        away = 1
        while True:
            if a+away >= size or matrix[a+away][b] >= point:
                if a + away >= size:
                    away -= 1
                total *= away
                break
            away += 1

        # left
        away = 1
        while True:
            if a-away < 0 or matrix[a-away][b] >= point:
                if a - away < 0:
                    away -= 1
                total *= away
                break
            away += 1

        # bottom
        away = 1
        while True:
            if b+away >= size or matrix[a][b+away] >= point:
                if b+away >= size:
                    away -= 1
                total *= away
                break
            away += 1

        # top
        away = 1
        while True:
            if b-away < 0 or matrix[a][b-away] >= point:
                if b-away < 0:
                    away -= 1
                total *= away
                break
            away += 1

        max_count = max(max_count, total)
print(max_count)