lines = []

# Read in stuff
with open("./files/input_18.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])


def add_parentheses(equation):
    index = 0
    new_equation = equation
    counter = 0
    while index < len(new_equation):
        if new_equation[index] == '(':
            counter += 1
            index += 1
            continue
        if new_equation[index] == ')' and counter != 0:
            counter -= 1
            index += 1
            continue
        if new_equation[index] != "+" or counter != 0:
            index += 1
            continue
        # insert lower paren
        a = index
        counter_inner = 0
        found_paren = False
        while a > 0:
            if new_equation[a] == '(':
                counter_inner -= 1
            if new_equation[a] == ')':
                counter_inner += 1
                found_paren = True
            if counter_inner == 0:
                if found_paren:
                    break
                elif new_equation[a] in "0123456789":
                    break
            a -= 1
        new_equation = new_equation[:a] + '(' + new_equation[a:]
        index += 1
        # insert upper paren
        b = index
        counter_inner = 0
        found_paren = False
        while b < len(new_equation)-1:
            if new_equation[b] == '(':
                counter_inner -= 1
            if new_equation[b] == ')':
                counter_inner += 1
                found_paren = True
            if counter_inner == 0:
                if found_paren:
                    break
                elif new_equation[b] in "0123456789":
                    break
            b += 1
        new_equation = new_equation[:b+1] + ')' + new_equation[b+1:]
        if a == 0 and b == len(new_equation)-2:
            new_equation = new_equation[1:-1]
            index -= 1
        index += 1
    return new_equation


def evaluate_equation(equation):
    new_equation = add_parentheses(equation)
    current_total = 0
    current_oper = '+'
    number_is_next = True
    is_in_paren = False
    mark = 0
    count = 0
    for index, c in enumerate(new_equation):
        num = None
        if c == '(':
            if count == 0:
                mark = index
                is_in_paren = True
            count += 1
        elif c == ')':
            count -= 1
            if count == 0:
                num = evaluate_equation(new_equation[mark+1:index])
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
