
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

    possible = sorted(possible, key=(lambda x: x[0][1] - x[0][0]), reverse=True)

    print(possible)

    for i in range(0, len(possible)):
        group = possible[i]
        for r in group:
            if set(record[r[0]:r[1]]) == {'#'}:
                possible[i] = [r]
                break

        group = possible[i]
        for j in range(i+1, len(possible)):
            later_group = possible[j]

            later_group_filtered = set()
            for item in later_group:
                check = True
                for item_first in group:
                    if len(set(range(item_first[0], item_first[1])).intersection(set(range(item[0], item[1])))) > 0:
                        check = False
                if check:
                    later_group_filtered.add(item)
            possible[j] = list(later_group_filtered)

    print(possible)
    lengths = [len(p) for p in possible]

