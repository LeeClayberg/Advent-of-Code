
# Read in stuff
with open("files/day07.txt", "r") as file_stream:
    rows = file_stream.readlines()
    rows = [row[:-1] for row in rows]

    beams = {rows[0].find('S')}
    splits = 0
    for row in rows[1:]:
        new_beams = beams
        for idx, cell in enumerate(row):
            if idx in beams and cell == '^':
                new_beams.update({idx - 1, idx + 1})
                new_beams.remove(idx)
                splits += 1
        beams = new_beams
    print(splits)





