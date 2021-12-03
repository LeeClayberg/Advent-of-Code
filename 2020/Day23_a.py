
cup_input = "137826495"
cups = list(map(lambda x: int(x), cup_input))

current_value = cups[0]
for move in range(100):
    # remove three next cups
    size = len(cups)
    remove = []
    for i in range(3):
        remove.append((cups.index(current_value) + i + 1) % size)
    remove.sort(reverse=True)
    picked_up = []
    counter = 0
    for idx in remove:
        if idx < cups.index(current_value):
            picked_up.insert(counter, cups.pop(idx))
        else:
            picked_up.insert(0, cups.pop(idx))
            counter +=1
    # select destination
    destination = current_value - 1
    while destination not in cups:
        if destination == 0:
            destination = max(cups)
        else:
            destination -= 1
    dest_index = cups.index(destination)
    current_value = cups[(cups.index(current_value)+1) % len(cups)]
    for cup in reversed(picked_up):
        cups.insert(dest_index+1, cup)
# end
index = cups.index(1)
answer = ""
for i in range(len(cups)-1):
    answer += str(cups[(index+i+1) % len(cups)])
print(answer)