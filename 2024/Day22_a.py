
# Read in stuff
with open("files/day22.txt", "r") as file_stream:
    # Setup
    starts = [int(line[:-1]) for line in file_stream.readlines()]

    total = 0
    for start in starts:
        secret = start
        for _ in range(2000):
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ (secret // 32)) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216
        total += secret
    print(total)