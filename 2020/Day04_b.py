import re

keyValues = []
valuesNeeded = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}


def is_valid(key_value):
    key = key_value.split(":")[0]
    val = key_value.split(":")[1]
    if key == 'byr':
        return len(val) == 4 and 1920 <= int(val) <= 2002
    elif key == 'iyr':
        return len(val) == 4 and 2010 <= int(val) <= 2020
    elif key == 'eyr':
        return len(val) == 4 and 2020 <= int(val) <= 2030
    elif key == 'hgt':
        end = val[-2:]
        if end == 'cm':
            return 150 <= int(val[:-2]) <= 193
        elif end == 'in':
            return 59 <= int(val[:-2]) <= 76
        else:
            return False
    elif key == 'hcl':
        return val[0] == '#' and len(val[1:]) == 6 and val[1:].isalnum()
    elif key == 'ecl':
        return val in "amb blu brn gry grn hzl oth"
    elif key == 'pid':
        return len(val) == 9 and val.isnumeric()
    elif key == 'cid':
        return True
    else:
        return False


# Read in stuff
with open("files/input_04.txt", "r") as file_stream:
    lines = file_stream.readlines()
    text = ''.join(lines)
    keyValues = re.split(" |\n", text)

keySet = set()
valid = 0
for keyValue in keyValues:
    if keyValue == '':
        if len(valuesNeeded.difference(keySet)) == 0:
            valid += 1
        keySet = set()
    else:
        if is_valid(keyValue):
            keySet.add(keyValue.split(':')[0])
print(valid)
