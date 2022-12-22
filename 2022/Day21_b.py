
monkeys = dict()
with open("files/input_21.txt", "r") as file_stream:
    counter = 0
    while True:
        line = file_stream.readline()
        if not line:
            break
        key, rest = line[:-1].split(': ')
        try:
            value = int(rest)
        except ValueError:
            num1, op, num2 = rest.split(' ')
            if op == '*':
                value = (lambda x, y: x * y, num1, num2, lambda z, x: int(z / x), lambda z, y: int(z / y))
            elif op == '-':
                value = (lambda x, y: x - y, num1, num2, lambda z, x: -(z - x), lambda z, y: z + y)
            elif op == '+':
                value = (lambda x, y: x + y, num1, num2, lambda z, x: z - x, lambda z, y: z - y)
            else:
                value = (lambda x, y: int(x / y), num1, num2, lambda z, x: x / z, lambda z, y: z * y)
        monkeys[key] = value


def calc_number(monkey):
    if monkey == 'humn':
        return lambda z: z
    data = monkeys[monkey]
    if isinstance(data, int):
        return data
    else:
        first = calc_number(data[1])
        second = calc_number(data[2])
        if isinstance(first, int) and isinstance(second, int):
            return data[0](first, second)
        elif isinstance(first, int):
            return lambda z: second(data[3](z, first))
        elif isinstance(second, int):
            return lambda z: first(data[4](z, second))
        raise Exception('Shouldn\'t get here')


root = monkeys['root']
right = calc_number(root[1])
left = calc_number(root[2])
if isinstance(right, int):
    print(left(right))
else:
    print(right(left))
