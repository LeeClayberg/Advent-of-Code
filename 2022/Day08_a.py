matrix = []
# Read in stuff
with open("files/input_08.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        matrix.append([int(x) for x in line[:-1]])

marked = [[0 for _ in row] for row in matrix]
size = len(matrix)

for a in range(size):
    max_left = -1
    max_right = -1
    max_top = -1
    max_bottom = -1
    for b in range(size):
        # From left
        if matrix[a][b] > max_left:
            max_left = matrix[a][b]
            marked[a][b] = 1
        # From right
        if matrix[a][-(b+1)] > max_right:
            max_right = matrix[a][-(b+1)]
            marked[a][-(b+1)] = 1
        # From top
        if matrix[b][a] > max_top:
            max_top = matrix[b][a]
            marked[b][a] = 1
        # From bottom
        if matrix[-(b+1)][a] > max_bottom:
            max_bottom = matrix[-(b+1)][a]
            marked[-(b+1)][a] = 1

print(sum([n for m in marked for n in m]))