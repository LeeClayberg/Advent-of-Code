lines = []

# Read in stuff
with open("files/input_18.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])


def evaluate_equation(equation):
    current_total = 0
    current_oper = '+'
    number_is_next = True
    is_in_paren = False
    mark = 0
    count = 0
    for index, c in enumerate(equation):
        num = None
        if c == '(':
            if count == 0:
                mark = index
                is_in_paren = True
            count += 1
        elif c == ')':
            count -= 1
            if count == 0:
                num = evaluate_equation(equation[mark+1:index])
                is_in_paren = False
        elif c == ' ':
            continue

        if not is_in_paren:
            if number_is_next:
                if num is None:
                    num = int(c)
                if current_oper == '+':
                    current_total += num
                else:
                    current_total *= num
            else:
                current_oper = c
            number_is_next = not number_is_next
    return current_total


total = 0
for line in lines:
    total += evaluate_equation(line)
print(total)
