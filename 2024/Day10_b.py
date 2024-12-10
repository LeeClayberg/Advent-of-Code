
# Read in stuff
with open("files/day10.txt", "r") as file_stream:
    lines = file_stream.readlines()
    grid = [[int(c) for c in line[:-1]] for line in lines]

    # Create map
    starts, ends = [], []
    ad_list = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 0:
                starts.append((x, y))
            if cell == 9:
                ends.append((x, y))
            neighbors = []
            for c_x, c_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                n_x, n_y = x + c_x, y + c_y
                if 0 <= n_x < len(row) and 0 <= n_y < len(grid):
                    if grid[n_y][n_x] == cell + 1:
                        neighbors.append((n_x, n_y))
            ad_list[(x, y)] = neighbors

    total = 0
    for start in starts:
        queue = [start]
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr in ends:
                total += 1
            queue += ad_list[curr]
    print(total)
