
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


total = 0
pair = 1
with open("files/input_13.txt", "r") as file_stream:
    while True:
        first = file_stream.readline()[:-1]
        if not first:
            break
        second = file_stream.readline()[:-1]
        file_stream.readline()

        first = parser(first)
        second = parser(second)

        compared = compare(first, second) > 0

        total += pair if compared else 0
        pair += 1

print(total)
