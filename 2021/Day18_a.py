import ast
import math

numbers = []
# Read in stuff
with open("files/input_18.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        numbers.append(line[:-1])


def add_to_closest(structure, value, adding_right):
    if isinstance(structure, list):
        if adding_right:
            return [add_to_closest(structure[0], value, adding_right), structure[1]]
        else:
            return [structure[0], add_to_closest(structure[1], value, adding_right)]
    else:
        return structure + value


def explode_one(structure, depth):
    if isinstance(structure, list):
        # Pair
        left, e1, la1, ra1 = explode_one(structure[0], depth+1)
        if e1:
            if ra1:
                return [left, add_to_closest(structure[1], ra1, True)], True, la1, None
            else:
                return [left, structure[1]], True, la1, None

        right, e2, la2, ra2 = explode_one(structure[1], depth+1)
        if e2:
            if la2:
                return [add_to_closest(structure[0], la2, False), right], True, None, ra2
            else:
                return [structure[0], right], True, None, ra2

        # Explode
        if depth >= 4:
            return 0, True, structure[0], structure[1]
        return [left, right], False, None, None
    else:
        return structure, False, None, None


def split_one(structure):
    if isinstance(structure, list):
        # Pair
        left, s1 = split_one(structure[0])
        if s1:
            return [left, structure[1]], True

        right, s2 = split_one(structure[1])
        if s2:
            return [structure[0], right], True

        return [left, right], False
    else:
        # Number
        if structure >= 10:
            return [math.floor(structure / 2), math.ceil(structure / 2)], True
        return structure, False


def simplify_number(structure):
    new_structure = structure
    last = ""
    while last != str(new_structure):
        last = str(new_structure)
        new_structure, success, _, _ = explode_one(new_structure, 0)
        if not success:
            new_structure, _ = split_one(new_structure)
    return new_structure


def number_magnitude(structure):
    if isinstance(structure, list):
        return 3 * number_magnitude(structure[0]) + 2 * number_magnitude(structure[1])
    else:
        return structure


total = ast.literal_eval(numbers[0])
for number in numbers[1:]:
    total = simplify_number([total, ast.literal_eval(number)])
print(number_magnitude(total))





