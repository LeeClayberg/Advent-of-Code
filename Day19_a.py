import re

lines = []

# Read in stuff
with open("./files/input_19.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

rules = lines[:138]
messages = lines[139:]

# set rules
rule_dict = dict()
for rule in rules:
    split_rule = re.split(': | \\| ', rule)
    sub_rules = []
    if split_rule[1][1] == 'a' or split_rule[1][1] == 'b':
        sub_rules = split_rule[1][1]
    else:
        for pair in split_rule[1:]:
            sub_rules.append(pair.split(' '))
    rule_dict[split_rule[0]] = sub_rules


# get all possibilities
def correct_forms(rule):
    forms = []
    rule_info = rule_dict[rule]
    if str(rule_info) in "ab":
        return [str(rule_info)]
    for option in rule_info:
        inner_forms = []
        for rule_num in option:
            if len(inner_forms) == 0:
                inner_forms = correct_forms(rule_num)
            else:
                new_inner_forms = []
                for in_lst in inner_forms:
                    for in_results in correct_forms(rule_num):
                        new_inner_forms.append(in_lst + in_results)
                inner_forms = new_inner_forms
        forms += inner_forms
    return forms

# check messages
all_correct_messages = correct_forms("0")
count = 0
for message in messages:
    if message in all_correct_messages:
        count += 1
print(count)
