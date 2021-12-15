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

shortest_matrix = [[10000000 for _ in range(len(matrix[i]))] for i in range(len(matrix))]

queue = [(0, (0, 0))]
heapq.heapify(queue)
while len(queue) > 0:
    sofar, point = heapq.heappop(queue)
    a, b = point
    if sofar + matrix[a][b] < shortest_matrix[a][b]:
        shortest_matrix[a][b] = sofar + matrix[a][b]
        for c, d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            e, f = a + c, b + d
            if e not in range(len(shortest_matrix)) or f not in range(len(shortest_matrix)):
                continue
            if shortest_matrix[a][b] + matrix[e][f] >= shortest_matrix[e][f]:
                continue
            heapq.heappush(queue, (shortest_matrix[a][b], (e, f)))
print(shortest_matrix[-1][-1] - matrix[0][0])
