lines = []

# Read in stuff
with open("files/input_22.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

player_1_stack = []
player_2_stack = []
is_player_1 = False
for line in lines:
    if "" == line:
        continue
    if "Player" in line:
        is_player_1 = not is_player_1
        continue
    if is_player_1:
        player_1_stack.append(int(line))
    else:
        player_2_stack.append(int(line))

while len(player_1_stack) > 0 and len(player_2_stack) > 0:
    player_1_top = player_1_stack.pop(0)
    player_2_top = player_2_stack.pop(0)
    if player_1_top > player_2_top:
        player_1_stack.append(player_1_top)
        player_1_stack.append(player_2_top)
    else:
        player_2_stack.append(player_2_top)
        player_2_stack.append(player_1_top)

player_1_is_winner = len(player_1_stack) > 0

winner_list = player_1_stack if player_1_is_winner else player_2_stack

total = 0
for idx, num in enumerate(reversed(winner_list)):
    total += (idx + 1) * num
print(total)