network = dict()
letter_counts = dict()

# Read in stuff
with open("files/input_14.txt", "r") as file_stream:
    base = list(file_stream.readline()[:-1])
    file_stream.readline()
    while True:
        line = file_stream.readline()
        if not line:
            break
        key, value = line[:-1].split(" -> ")
        network[key] = (value, [key[0] + value, value + key[1]])

queue = []
for i in range(len(base) - 1):
    queue.append((''.join(base[i:i + 2])))

seen_before = dict()


def recursive_part(key, depth):
    if depth < 40:
        if (key, depth) in seen_before.keys():
            return seen_before[(key, depth)]
        char, next_keys = network[key]
        left = recursive_part(next_keys[0], depth + 1)
        right = recursive_part(next_keys[1], depth + 1)
        total = dict()
        for l_key in left.keys():
            if l_key not in total.keys():
                total[l_key] = 0
            total[l_key] += left[l_key]
        for r_key in right.keys():
            if r_key not in total.keys():
                total[r_key] = 0
            total[r_key] += right[r_key]
        if char not in total.keys():
            total[char] = 0
        total[char] += 1
        seen_before[(key, depth)] = total
        return total
    else:
        return dict()


# Get recursive counts
values = [recursive_part(a, 0) for a in queue]
for value in values:
    for k in value.keys():
        if k not in letter_counts.keys():
            letter_counts[k] = 0
        letter_counts[k] += value[k]

# Add original letters to counts
for char in base:
    if char not in letter_counts.keys():
        letter_counts[char] = 0
    letter_counts[char] += 1

sorted_counts = sorted(letter_counts.items(), key=lambda x: x[1])
print(sorted_counts[-1][1] - sorted_counts[0][1])
