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


def recurisive_combat(player_1, player_2):
    player_1_past = []
    player_2_past = []
    player_1_hand = player_1
    player_2_hand = player_2
    while len(player_1_hand) > 0 and len(player_2_hand) > 0:
        # first rule
        if player_1_hand in player_1_past and player_2_hand in player_2_past and player_1_past.index(player_1_hand) == player_2_past.index(player_2_hand):
            return {"winner_is_1": True, "hand": player_1_hand}
        player_1_past.append(player_1_hand.copy())
        player_2_past.append(player_2_hand.copy())
        # second rule
        player_1_top = player_1_hand.pop(0)
        player_2_top = player_2_hand.pop(0)
        # third rule
        if len(player_1_hand) >= player_1_top and len(player_2_hand) >= player_2_top:
            round_winner = recurisive_combat(player_1_hand[:player_1_top], player_2_hand[:player_2_top])['winner_is_1']
        else:
            round_winner = player_1_top > player_2_top
        # fourth rule
        if round_winner:
            player_1_hand.append(player_1_top)
            player_1_hand.append(player_2_top)
        else:
            player_2_hand.append(player_2_top)
            player_2_hand.append(player_1_top)

    player_1_is_winner = len(player_1_hand) > 0
    winner_list = player_1_hand if player_1_is_winner else player_2_hand
    return {"winner_is_1": player_1_is_winner, "hand": winner_list}


game_winner_hand = recurisive_combat(player_1_stack, player_2_stack)["hand"]

total = 0
for idx, num in enumerate(reversed(game_winner_hand)):
    total += (idx + 1) * num
print(total)
