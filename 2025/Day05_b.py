
# Read in stuff
with open("files/day05.txt", "r") as file_stream:
    data = file_stream.read()
    ranges = [line.split('-') for line in data.split('\n\n')[0].split('\n')]
    ranges = [(int(rng[0]), int(rng[1])) for rng in ranges]

    ranges.sort(key=lambda x: x[0])

    idx = 0
    while idx < len(ranges)-1:
        n_start, n_end = ranges[idx]
        n1_start, n1_end = ranges[idx+1]

        if n_start <= n1_start <= n_end:
            if not(n_start <= n1_end <= n_end):
                ranges[idx] = (n_start, n1_end)
            ranges.pop(idx + 1)
        else:
            idx +=1

    count = 0
    for start, end in ranges:
        count += end - start + 1
    print(count)
