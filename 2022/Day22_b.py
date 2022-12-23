
grid = []
with open("files/input_22.txt", "r") as file_stream:
    width = 0
    while True:
        line = file_stream.readline()
        if not line:
            break
        if line == '\n':
            line = file_stream.readline()
            code_instructions = line[:-1]
            continue
        row = line[:-1]
        if len(row) > width:
            width = len(row)
            grid = [r + [' ' for _ in range(width - len(r))] for r in grid]
        full_row = list(row) + [' ' for _ in range(width - len(row))]
        grid.append(full_row)

# Starting position
position = next((x, 0, 0) for x in range(len(grid[0])) if grid[0][x] == '.')