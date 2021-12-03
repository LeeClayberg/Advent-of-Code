
values = [0,20,7,16,1,18,15]

round = 1
saver = dict()
last_number = values[0]
current_number = 0
while round <= 2020:
    if round < len(values):
        current_number = values[round]
    elif last_number not in saver.keys():
        current_number = 0
    elif last_number in saver.keys():
        current_number = (round - 1) - saver[last_number]
    if round == 2020:
        print(last_number)
    saver[last_number] = round - 1
    last_number = current_number
    round += 1