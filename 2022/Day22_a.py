
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

# Parse instructions
instructions = []
current = ''
for char in code_instructions:
    if char.isnumeric():
        current += char
    else:
        if len(current) > 0:
            instructions.append(int(current))
            current = ''
        instructions += char
if len(current) > 0:
    instructions.append(int(current))

# Loop through instructions
for instruction in instructions:
    if isinstance(instruction, int):
        counter = instruction
        stage_position = position
        while counter > 0:
            # Update position
            x, y, rot = position
            if rot == 0:
                new_x = (x + 1) % len(grid[0])
                new_position = (new_x, y, rot)
            elif rot == 2:
                new_x = (x - 1) % len(grid[0])
                new_position = (new_x, y, rot)
            elif rot == 1:
                new_y = (y + 1) % len(grid)
                new_position = (x, new_y, rot)
            else:
                new_y = (y - 1) % len(grid)
                new_position = (x, new_y, rot)
            n_x, n_y, n_rot = new_position
            # Exit if wall is hit
            if grid[n_y][n_x] == '#':
                break
            position = new_position
            # Only update stage if not outside map
            if grid[n_y][n_x] != ' ':
                stage_position = position
                counter -= 1
        position = stage_position
    else:
        if instruction == 'R':
            new_rotation = (position[2] + 1) % 4
        else:
            new_rotation = (position[2] - 1) % 4
        position = (position[0], position[1], new_rotation)

final_x, final_y, final_rot = position
total = (final_y + 1) * 1000 + (final_x + 1) * 4 + final_rot
print(total)
