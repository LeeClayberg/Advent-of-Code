
# Read in stuff
with open("files/day08.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    antennas = {}
    height, wide = len(lines), len(lines[0])
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == '.':
                continue
            if cell not in antennas:
                antennas[cell] = []
            antennas[cell].append((x, y))

    antinodes = set()
    for positions in antennas.values():
        length = len(positions)
        for a in range(0, length):
            for b in range(0, length):
                if a == b:
                    continue
                ant1, ant2 = positions[a], positions[b]
                slope = (ant1[0] - ant2[0], ant1[1] - ant2[1])
                while 0 <= ant1[0] < wide and 0 <= ant1[1] < height:
                    antinodes.add(ant1)
                    ant1 = (ant1[0] + slope[0], ant1[1] + slope[1])
                while 0 <= ant2[0] < wide and 0 <= ant2[1] < height:
                    antinodes.add(ant2)
                    ant2 = (ant2[0] - slope[0], ant2[1] - slope[1])

    print(len(antinodes))


