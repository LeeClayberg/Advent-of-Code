
# Read in stuff
with open("files/day22.txt", "r") as file_stream:
    # Setup
    starts = [int(line[:-1]) for line in file_stream.readlines()]

    bananas = {}
    for start in starts:
        secret = start
        secrets = [int(str(secret)[-1])]
        for _ in range(2000):
            secret = (secret ^ (secret * 64)) % 16777216
            secret = (secret ^ (secret // 32)) % 16777216
            secret = (secret ^ (secret * 2048)) % 16777216
            secrets.append(int(str(secret)[-1]))

        price_changes = [secrets[i+1] - secrets[i] for i in range(0, len(secrets)-1)]

        seen = set()
        for i in range(0, len(price_changes)-3):
            sequence = (price_changes[i], price_changes[i+1], price_changes[i+2], price_changes[i+3])
            if sequence in seen:
                continue
            seen.add(sequence)
            if sequence not in bananas:
                bananas[sequence] = 0
            bananas[sequence] += secrets[i+4]
    print(max(bananas.items(), key=(lambda b: b[1])))
