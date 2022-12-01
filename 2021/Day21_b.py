
seen = dict()

amount = 21


def find_win_counts(player_1_position, player_2_position, player_1_score, player_2_score, player_1_turn):
    key = (player_1_position, player_2_position, player_1_score, player_2_score, player_1_turn)
    if key in seen.keys():
        return seen[key]
    if player_1_score >= amount:
        return 1, 0
    if player_2_score >= amount:
        return 0, 1
    total = (0, 0)
    for dice_roll in range(1, 4):
        if player_1_turn:
            new_p1p = (player_1_position + dice_roll) % 10
            new_p1s = player_1_score + new_p1p + 1
            new_p2p = player_2_position
            new_p2s = player_2_score
        else:
            new_p1p = player_1_position
            new_p1s = player_1_score
            new_p2p = (player_2_position + dice_roll) % 10
            new_p2s = player_2_score + new_p2p + 1
        new_pt = not player_1_turn
        p1_wins, p2_wins = find_win_counts(new_p1p, new_p2p, new_p1s, new_p2s, new_pt)
        total = (total[0] + p1_wins, total[1] + p2_wins)
    seen[key] = total
    return total


print(find_win_counts(7, 1, 0, 0, True))
