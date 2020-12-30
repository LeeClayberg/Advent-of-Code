
card_public_key = 3418282
door_public_key = 8719412

subject_number = 7

card_loop_count = 0
door_loop_count = 0

# find loop counts
current_value = 1
while True:
    current_value = (current_value * subject_number) % 20201227
    card_loop_count += 1
    if current_value == card_public_key:
        break

current_value = 1
while True:
    current_value = (current_value * subject_number) % 20201227
    door_loop_count += 1
    if current_value == door_public_key:
        break

# calc encryption key
current_value = 1
for i in range(card_loop_count):
    current_value = (current_value * door_public_key) % 20201227
print(current_value)
# check encryption key
current_value = 1
for i in range(door_loop_count):
    current_value = (current_value * card_public_key) % 20201227
print(current_value)

