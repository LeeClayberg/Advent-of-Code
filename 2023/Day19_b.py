

with open("files/day19.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    separator = lines.index('')
    workflows = lines[:separator]

    combinations = []

    # Create functions
    workflow_funcs = {}
    for workflow in workflows:
        w_key, rest = workflow.split('{')
        rest = rest[:-1]
        rules = rest.split(',')
        rules, base_case = rules[:-1], rules[-1]

        rule_funcs = []
        for rule in rules:
            func, dest = rule.split(':')
            parts = func.split('>')
            if len(parts) > 1:
                r_key, amount = parts
                amount = int(amount)
                def compare1(t, r_key=r_key, amount=amount):
                    passed = t.copy()
                    start, end = passed[r_key]
                    if start < amount < end:
                        passed[r_key] = (amount+1, end)
                        t[r_key] = (start, amount)
                        return passed
                    else:
                        t[r_key] = (0, 0)
                        return passed
                # print(f'(lambda t: t["{r_key}"] > {int(amount)}, "{dest}")')
                rule_funcs.append((compare1, dest))
            else:
                r_key, amount = func.split('<')
                amount = int(amount)
                def compare2(t, r_key=r_key, amount=amount):
                    passed = t.copy()
                    start, end = passed[r_key]
                    if start < amount < end:
                        passed[r_key] = (start, amount-1)
                        t[r_key] = (amount, end)
                        return passed
                    else:
                        t[r_key] = (0, 0)
                        return passed
                # print(f'(lambda t: t["{r_key}"] < {int(amount)}, "{dest}")')
                rule_funcs.append((compare2, dest))
        def workflow_func(data, rule_funcs=rule_funcs, base_case=base_case):
            new_data = data
            for rule_func, dest_key in rule_funcs:
                passed = rule_func(new_data)
                if dest_key in ['A', 'R']:
                    combinations.append(passed)
                else:
                    workflow_funcs[dest_key](passed)
            if base_case in ['A', 'R']:
                if base_case == 'A':
                    combinations.append(new_data)
            else:
                workflow_funcs[base_case](new_data)

        workflow_funcs[w_key] = workflow_func

    data = {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}

    print(workflow_funcs)
    workflow_funcs['in'](data)

    total = 0
    for entry in combinations:
        sub_total = 1
        for start, end in entry.values():
            sub_total *= (end - start)
        total += sub_total
    print(total)

    total = 0
    for i, row in enumerate(combinations):
        x, m, a, s = row['x'], row['m'], row['a'], row['s']
        x = set(range(x[0], x[1]))
        m = set(range(m[0], m[1]))
        a = set(range(a[0], a[1]))
        s = set(range(s[0], s[1]))
        for j, row_2 in enumerate(combinations[i:]):
            x2, m2, a2, s2 = row_2['x'], row_2['m'], row_2['a'], row_2['s']
            x.difference_update(set(range(x2[0], x2[1])))
            m.difference_update(set(range(m2[0], m2[1])))
            a.difference_update(set(range(a2[0], a2[1])))
            s.difference_update(set(range(s2[0], s2[1])))
        sub_total = len(x) * len(m) * len(a) * len(s)
        print(sub_total)
    print()
    print(total)