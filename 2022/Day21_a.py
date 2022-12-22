
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
                value = (lambda x, y: x * y, num1, num2)
            elif op == '-':
                value = (lambda x, y: x - y, num1, num2)
            elif op == '+':
                value = (lambda x, y: x + y, num1, num2)
            else:
                value = (lambda x, y: int(x / y), num1, num2)
        monkeys[key] = value


def calc_number(monkey):
    data = monkeys[monkey]
    if isinstance(data, int):
        return data
    else:
        return data[0](calc_number(data[1]), calc_number(data[2]))


answer = calc_number('root')
print(answer)