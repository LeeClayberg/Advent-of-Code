import re

with open("files/day12.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

total = 0
for l, line in enumerate(lines):
    record, groups = line.split(' ')
    groups = [int(a) for a in groups.split(',')]
    groups_seen = [False for _ in groups]

    sections = [section for section in re.split('[.]+', record) if section != '']
    section_groups = [set() for _ in sections]

    group_start_idx = 0
    section_idx = 0
    while section_idx < len(sections):
        section = sections[section_idx]
        start_check = sum([len(sec) for sec in sections[:section_idx+1]])
        for group_idx in range(group_start_idx, len(groups)):
            group = groups[group_idx]
            start = sum(groups[:group_idx]) + len(groups[:group_idx]) - section_idx
            if start >= start_check:
                break
            if group > len(section):
                continue
            found_working = False
            for frame_start in range(0, len(section) - group+1):
                frame = section[frame_start:frame_start+ group]

                before = frame_start > 0 and section[frame_start - 1] == '#'
                after = frame_start + group < len(section) and section[frame_start + group] == '#'
                if not (before or after):
                    if frame[0] == '#' and not groups_seen[group_idx]:
                        # update sections
                        if section != frame:
                            before, after = section.split(frame, 1)
                            before, after = before[:-1], after[1:]
                            if len(before) > 0:
                                sections[section_idx] = before
                                section_idx += 1
                                sections.insert(section_idx, frame)
                                section_groups.insert(section_idx, {group_idx})
                            else:
                                sections[section_idx] = frame
                                section_groups[section_idx] = {group_idx}
                            if len(after) > 0:
                                sections.insert(section_idx + 1, after)
                                section_groups.insert(section_idx + 1, set())
                        else:
                            section_groups[section_idx].add(group_idx)
                        group_start_idx = group_idx + 1
                        found_working = True
                        break
                    else:
                        section_groups[section_idx].add(group_idx)
                    groups_seen[group_idx] = True
            if found_working:
                break
        section_idx += 1

    # fix groups
    for before_idx in reversed(range(0, len(section_groups))):
        before_section = sections[before_idx]
        before_groups = section_groups[before_idx]
        if len(before_groups) > 1:
            before_groups = sorted(list(before_groups), reverse=True)
            can_fit = set()
            for before_group in before_groups:
                fit_length = sum([groups[idx] for idx in can_fit]) + len(can_fit) + groups[before_group]
                if fit_length <= len(before_section):
                    can_fit.add(before_group)
                else:
                    break
            section_groups[before_idx] = can_fit

    print(sections)
    print(section_groups)

    sub_total = 1
    for section, group_indices in zip(sections, section_groups):
        if set(list(section)) != {'?'}:
            continue

        if len(group_indices) == 1:
            combinations = len(section) - groups[list(group_indices)[0]] + 1
        else:
            group_taken = sum([groups[idx] for idx in group_indices])
            free_spaces = len(section) - group_taken
            combinations = sum(a for a in range(1, free_spaces+1))
        sub_total *= combinations
    print(sub_total)
    total += sub_total