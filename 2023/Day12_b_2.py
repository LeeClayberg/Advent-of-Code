
with open("files/day12.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

total = 0
for line in lines:
    record, groups = line.split(' ')
    groups = [int(a) for a in groups.split(',')]

    possible = [[] for _ in groups]
    idx = 0
    group_idx = 0
    while group_idx < len(groups):
        end = 0
        if group_idx < len(groups) - 1:
            end = sum(groups[group_idx+1:]) + len(groups[group_idx+1:])
        while idx+groups[group_idx] <= len(record) - end:
            group = groups[group_idx]
            sub_record = record[idx:idx+group]

            if '.' not in sub_record:
                if sub_record[0] == '?':
                    possible[group_idx].append((idx, idx + group))
                    idx += 1
                if sub_record[0] == '#':
                    possible[group_idx].append((idx, idx + group))
                    break
            else:
                idx += 1

        idx = possible[group_idx][0][1] + 1
        group_idx += 1

    print(possible)

    possible = sorted(possible, key=(lambda x: len(x)))

    for p in range(0, len(possible)):
        group = possible[p]
        for r in group:
            if set(record[r[0]:r[1]]) == {'#'}:
                possible[p] = [r]
                break
        if len(possible[p]) == 1:
            for option in group:
                for o, other_group in enumerate(possible[p+1:]):
                    other_option_idx = 0
                    while other_option_idx < len(other_group):
                        other_option = other_group[other_option_idx]
                        full_option_space = range(option[0]-1, option[1]+1)
                        check1 = other_option[0] in full_option_space
                        check2 = other_option[1]-1 in full_option_space
                        if check1 or check2:
                            other_group.remove(other_option)
                        else:
                            other_option_idx += 1
    print(possible)