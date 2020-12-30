import re

lines = []


def count_bags(colors, current_key):
    if len(colors[current_key]) > 0:
        sub_total = 1
        for entry in colors[current_key]:
            sub_total += int(entry['count']) * count_bags(colors, entry['key'])
        return sub_total
    else:
        return 1


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
print(count_bags(bag_dict, 'shiny gold')-1)
