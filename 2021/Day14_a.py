
replacements = dict()

# Read in stuff
with open("files/input_14.txt", "r") as file_stream:
    base = list(file_stream.readline()[:-1])
    file_stream.readline()
    while True:
        line = file_stream.readline()
        if not line:
            break
        key, value = line[:-1].split(" -> ")
        replacements[key] = value

for step in range(10):
    i = 0
    while i < len(base)-1:
        piece = ''.join(base[i:i+2])
        if piece in replacements.keys():
            base.insert(i+1, replacements[piece])
            i += 1
        i += 1

counts = dict()
for char in base:
    if char not in counts.keys():
        counts[char] = 0
    counts[char] += 1

sorted_counts = sorted(counts.items(), key=lambda x: x[1])
print(sorted_counts)
print(sorted_counts[-1][1] - sorted_counts[0][1])
