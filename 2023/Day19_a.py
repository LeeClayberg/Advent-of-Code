

with open("files/day19.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    separator = lines.index('')
    workflows = lines[:separator]
    ratings = lines[separator+1:]

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
                def compare1(t, r_key=r_key, amount=amount):
                    return t[r_key] > int(amount)
                # print(f'(lambda t: t["{r_key}"] > {int(amount)}, "{dest}")')
                rule_funcs.append((compare1, dest))
            else:
                r_key, amount = func.split('<')
                def compare2(t, r_key=r_key, amount=amount):
                    return t[r_key] < int(amount)
                # print(f'(lambda t: t["{r_key}"] < {int(amount)}, "{dest}")')
                rule_funcs.append((compare2, dest))
        def workflow_func(data, rule_funcs=rule_funcs, base_case=base_case):
            for rule_func, dest_key in rule_funcs:
                result = rule_func(data)
                if result:
                    return dest_key
            return base_case

        workflow_funcs[w_key] = workflow_func

    # Run input on functions
    total = 0
    for rating in ratings:
        rating_inner = rating[1:-1]
        pairs = rating_inner.split(',')

        data_map = {}
        for pair in pairs:
            key, value = pair.split('=')
            data_map[key] = int(value)

        next_key = 'in'
        while next_key not in ['A', 'R']:
            curr_func = workflow_funcs[next_key]
            next_key_1 = curr_func(data_map)
            next_key = next_key_1
        total += 0 if next_key == 'R' else sum(data_map.values())
    print(total)