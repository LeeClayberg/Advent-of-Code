
with open("files/day14.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    columns = [''.join([line[a] for line in lines]) for a in range(0, len(lines[0]))]

    total = 0
    for column in columns:
        sections = column.split('#')
        for s in range(0, len(sections)):
            section = list(sections[s])
            section.sort(reverse=True)
            section = ''.join(section)
            sections[s] = section
        tilted_column = '#'.join(sections)
        for i, spot in enumerate(tilted_column):
            if spot == 'O':
                total += len(tilted_column) - i
    print(total)
