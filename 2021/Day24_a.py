import ast
import math

operations = []
# Read in stuff
with open("files/input_24.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        converted = line[:-1].split()
        try:
            converted[-1] = int(converted[-1])
        except Exception:
            converted[-1] = converted[-1]
        operations.append(tuple(converted))

print(operations)

i = 99999999999999
while True:
    parts = list(map(lambda d: int(d), str(i)))
    stored_values = dict()
    part_counter = 0
    for operation in operations:
        if operation[0] == 'inp':
            stored_values["w"] = parts[part_counter]
            part_counter += 1
        else:
            print(stored_values)
            print(operation)
            action, var_1, var_2 = operation
            if not isinstance(var_1, int) and var_1 not in stored_values.keys():
                stored_values[var_1] = 0
            if not isinstance(var_2, int) and var_2 not in stored_values.keys():
                stored_values[var_2] = 0

            var_1 = stored_values[var_1]
            if not isinstance(var_2, int):
                var_2 = stored_values[var_2]

            if action == "add":
                stored_values[var_1] = var_1 + var_2
            elif action == "mul":
                stored_values[var_1] = var_1 * var_2
            elif action == "div":
                stored_values[var_1] = var_1 / var_2
            elif action == "mod":
                stored_values[var_1] = var_1 % var_2
            elif action == "eql":
                stored_values[var_1] = 1 if var_1 == var_2 else 0
    print(stored_values)
    if stored_values["z"] == 0:
        print(i)
        break
    else:
        print(stored_values)
        i -= 1
