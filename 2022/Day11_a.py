
def create_function(operator, number):
    if operator == '*':
        return lambda num: num * (int(number) if number != 'old' else num)
    else:
        return lambda num: num + (int(number) if number != 'old' else num)


monkeys = dict()
with open("files/input_11.txt", "r") as file_stream:
    while True:
        label = file_stream.readline()
        if not label:
            break
        monkey_num = int(label[:-2].split(' ')[-1])
        items_line = file_stream.readline()
        items = [int(i) for i in items_line[:-1].split(': ')[1].split(',')]
        func_line = file_stream.readline()[:-1].split(' ')
        func = create_function(func_line[-2], func_line[-1])
        test = int(file_stream.readline()[:-1].split(' ')[-1])
        true_case = int(file_stream.readline()[:-1].split(' ')[-1])
        false_case = int(file_stream.readline()[:-1].split(' ')[-1])
        _ = file_stream.readline()
        monkeys[monkey_num] = {
            'items': items,
            'operation': func,
            'test': test,
            'true': true_case,
            'false': false_case,
        }

active = dict()
for r in range(20):
    for key in monkeys.keys():
        value = monkeys[key]
        if key not in active.keys():
            active[key] = 0
        items_count = len(value['items'])
        active[key] += items_count

        while len(value['items']) > 0:
            item = value['items'].pop(0)
            worry_level = value['operation'](item)
            bored = worry_level // 3
            thrown_to = value['true'] if bored % value['test'] == 0 else value['false']
            monkeys[thrown_to]['items'].append(bored)

num1, num2 = sorted(active.values())[-2:]
print(num1 * num2)


