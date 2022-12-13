import functools

def parser(string):
    if '[' not in string:
        return int(string)
    else:
        inner = string[1:-1]
        depth = 0
        last = 0
        parts = []
        if len(inner) > 0:
            for i in range(len(inner)):
                if inner[i] == "," and depth == 0:
                    parts.append(parser(inner[last:i]))
                    last = i + 1
                if inner[i] == "[":
                    depth += 1
                elif inner[i] == "]":
                    depth -= 1
            parts.append(parser(inner[last:]))
        return parts


def compare(one, two):
    if isinstance(one, int) and isinstance(two, int):
        # pos = correct, zero = equal, neg = incorrect
        return two - one
    if isinstance(one, int):
        return compare([one], two)
    elif isinstance(two, int):
        return compare(one, [two])

    for i in range(len(one)):
        if i >= len(two):
            return -1
        compared = compare(one[i], two[i])
        if compared > 0:
            return 1
        elif compared < 0:
            return -1
    return 1 if len(one) < len(two) else 0


divider_1 = [[2]]
divider_2 = [[6]]
packets = [divider_1, divider_2]
with open("files/input_13.txt", "r") as file_stream:
    while True:
        first = file_stream.readline()[:-1]
        if not first:
            break
        second = file_stream.readline()[:-1]
        file_stream.readline()

        first = parser(first)
        packets.append(first)

        second = parser(second)
        packets.append(second)

sorted_packets = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)

divider_indices = []
for idx, packet in enumerate(sorted_packets):
    if packet in [divider_1, divider_2]:
        divider_indices.append(idx+1)

print(divider_indices[0] * divider_indices[1])
