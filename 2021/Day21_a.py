import ast
import math

player_1_position = 7
player_2_position = 1

player_1_score = 0
player_2_score = 0

player_1_turn = True
current_point = 0
die_rolls = 0
while player_1_score < 1000 and player_2_score < 1000:
    subscore = 0
    for _ in range(3):
        subscore += current_point
        current_point = (current_point + 1) % 100
    subscore += 3
    die_rolls += 3
    if player_1_turn:
        player_1_position = (player_1_position + subscore) % 10
        player_1_score += player_1_position + 1
    else:
        player_2_position = (player_2_position + subscore) % 10
        player_2_score += player_2_position + 1
    player_1_turn = not player_1_turn
loser = min(player_1_score, player_2_score)
print(loser * die_rolls)
