
with open("files/day12.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

def arrangements(data, saved, record_str, layer):
    if len(data) == 0:
        return 0 if '#' in record_str else 1
    first, rest = data[0], data[1:]
    sub_total = 0
    for item in first:
        if '#' in record_str[:item[0]]:
            continue
        filler = '*' * (item[1] - item[0])
        new_record_str = filler.join([record_str[:item[0]], record_str[item[1]:]])
        filtered_rest = []
        for rest_other in rest:
            filtered_other = []
            for other_spot in rest_other:
                if other_spot[0] > item[1]:
                    filtered_other.append(other_spot)
            if len(filtered_other) > 0:
                filtered_rest.append(filtered_other)

        key = str(layer) + str(item)
        if '#' not in record_str and key in saved:
            arrange = saved[key]
        else:
            arrange = arrangements(filtered_rest, saved, new_record_str, layer+1)
            if '#' not in record_str:
                saved[key] = arrange
        sub_total += arrange
    return sub_total


total = 0
for l, line in enumerate(lines):
    record, groups = line.split(' ')
    groups = [int(a) for a in groups.split(',')]

    record = [record] * 5
    record = '?'.join(record)

    groups *= 5

    # Add possible spots
    record += '.'
    possible = [[] for _ in groups]
    for g, group in enumerate(groups):
        idx = 0
        if g > 0:
            idx = possible[g - 1][0][0] + groups[g - 1] + 1
        while idx < len(record)-group:
            sub_record = record[idx:idx+group]
            if '.' not in sub_record:
                before = idx > 0 and record[idx-1] == '#'
                after = idx+group < len(record) and record[idx+group] == '#'
                if not (before or after):
                    possible[g].append((idx, idx + group))
            idx += 1

    # Remove spots that collide with ones that can only go in one spot
    queue = list(filter(lambda x: len(x) == 1, possible))
    while len(queue) > 0:
        single = queue.pop(0)[0]
        single_range = set(range(single[0] - 1, single[1] + 1))
        for sub_possible in possible:
            if len(sub_possible) == 1:
                continue
            else:
                ps_idx = 0
                while ps_idx < len(sub_possible):
                    ps_range = sub_possible[ps_idx]
                    ps_range = set(range(ps_range[0], ps_range[1]))

                    collide = len(single_range.intersection(ps_range)) > 0
                    if collide:
                        sub_possible.pop(ps_idx)
                    else:
                        ps_idx += 1
                if len(sub_possible) == 1:
                    queue.append(sub_possible)

    # Remove any that are out of range
    possible = list(reversed(possible))
    for s, sub_possible in enumerate(possible[:-1]):
        max_spot = sub_possible[-1][0]
        for other in possible[s+1:]:
            ps_idx = 0
            while ps_idx < len(other):
                ps_spot = other[ps_idx]

                collide = ps_spot[1] > max_spot - 1
                if collide:
                    other.pop(ps_idx)
                else:
                    ps_idx += 1

    possible = list(reversed(possible))

    save_dict = {}
    variations = arrangements(possible, save_dict, record, 0)
    print(l+1, variations, possible)

    total += variations

print(total)
