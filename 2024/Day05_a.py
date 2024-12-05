
# Read in stuff
with open("files/day05.txt", "r") as file_stream:
    lines = file_stream.readlines()
    rules = {}
    updates = []
    add_to_rules = True
    for line in lines:
        if line == '\n':
            add_to_rules = False
            continue
        if add_to_rules:
            before, after = line[:-1].split('|')
            if before not in rules:
                rules[before] = set()
            rules[before].add(after)
        else:
            updates.append(line[:-1].split(','))

    total = 0
    for update in updates:
        check = True
        for idx, num in enumerate(update):
            if len(rules[num].intersection(set(update[:idx]))) > 0:
                check = False
                break
        if check:
            total += int(update[len(update) // 2])
    print(total)