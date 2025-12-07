
# Read in stuff
with open("files/day05.txt", "r") as file_stream:
    data = file_stream.read()
    ranges = [line.split('-') for line in data.split('\n\n')[0].split('\n')]
    ranges = [(int(rng[0]), int(rng[1])) for rng in ranges]
    ids = [int(line) for line in data.split('\n\n')[1].split('\n')[:-1]]

    fresh = 0
    for iid in ids:
        for start, end in ranges:
            if start <= iid <= end:
                fresh +=1
                break
    print(fresh)