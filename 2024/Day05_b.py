
# Read in stuff
with open("files/day05.txt", "r") as file_stream:
    lines = file_stream.readlines()

    # Create rules and updates
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

    # Get unordered
    unordered = []
    for update in updates:
        check = True
        for idx, num in enumerate(update):
            if num not in rules:
                continue
            if len(rules[num].intersection(set(update[:idx]))) > 0:
                check = False
                break
        if not check:
            unordered.append(update)

    # Sort unordered
    ordered = []
    for update in unordered:
        new_update = [a for a in update]
        i = 0
        while i < len(new_update):
            j = i
            while new_update[j] in rules and len(rules[new_update[j]].intersection(set(new_update[:j]))) > 0:
                new_update.insert(j-1, new_update.pop(j))
                j -= 1
            i += 1
        ordered.append(new_update)

    # Find total of middles
    total = 0
    for update in ordered:
        total += int(update[len(update) // 2])
    print(total)
