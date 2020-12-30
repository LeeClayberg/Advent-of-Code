import re

lines = []


def find_gold_bag(colors, current_key):
    if len(colors[current_key]) > 0:
        found = False
        for entry in colors[current_key]:
            found |= entry['key'] == 'shiny gold' or find_gold_bag(colors, entry['key'])
            if found:
                break
        return found
    else:
        return False


# Read in stuff
with open("./files/input_07.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            lines.append('')
            break
        lines.append(line[:-1])

bag_dict = dict()
for line in lines[:-1]:
    parts = re.split(" bags contain |, ", line)
    new_color = parts[0]
    contain_bags = []
    if parts[1] != "no other bags.":
        for contain in parts[1:]:
            num_color = contain.split(" bag")[0]
            inner_parts = num_color.split(" ", 1)
            contain_bags.append({"count": inner_parts[0], "key": inner_parts[1]})
    bag_dict[new_color] = contain_bags

count = 0
for key in bag_dict.keys():
    if find_gold_bag(bag_dict, key):
        count += 1
print(count)
