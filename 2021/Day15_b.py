import copy
import heapq
matrix = []

# Read in stuff
with open("files/input_15.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        row = list(map(lambda x: int(x), line[:-1]))
        matrix.append(row)

full_row = copy.deepcopy(matrix)
for i in range(1, 9):
    for a in range(len(full_row)):
        full_row[a].extend(list(map(lambda x: (x+i-1) % 9 + 1, matrix[a])))

section_size = len(matrix)
full_matrix = []
for b in range(5):
    for row in full_row:
        full_matrix.append(row[section_size*b:section_size*(b+5)])

shortest_matrix = [[100000 for _ in range(len(full_matrix[i]))] for i in range(len(full_matrix))]

queue = [(0, (0, 0))]
heapq.heapify(queue)
while len(queue) > 0:
    sofar, point = heapq.heappop(queue)
    a, b = point
    if sofar + full_matrix[a][b] < shortest_matrix[a][b]:
        shortest_matrix[a][b] = sofar + full_matrix[a][b]
        for c, d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            e, f = a + c, b + d
            if e not in range(len(shortest_matrix)) or f not in range(len(shortest_matrix)):
                continue
            if shortest_matrix[a][b] + full_matrix[e][f] >= shortest_matrix[e][f]:
                continue
            heapq.heappush(queue, (shortest_matrix[a][b], (e, f)))
print(shortest_matrix[-1][-1] - full_matrix[0][0])
