
# Read in stuff
with open("files/day11.txt", "r") as file_stream:
    line = file_stream.read()
    stones = [int(s) for s in line[:-1].split(' ')]
    blinks = 75


cache = {}

def calc_stone(stone, blink):
    # Check cache
    key = f"{stone}_{blink}"
    if key in cache:
        return cache[key]
    # Base
    if blink == 0:
        return 1
    # Recursive
    if stone == 0:
        calc = calc_stone(1, blink-1)
        cache[key] = calc
        return calc
    elif len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        len_stone = len(str_stone)
        left, right = str_stone[:len_stone // 2], str_stone[len_stone // 2:]
        calc_left = calc_stone(int(left), blink-1)
        calc_right = calc_stone(int(right), blink-1)
        calc = calc_left + calc_right
        cache[key] = calc
        return calc_left + calc_right
    else:
        calc = calc_stone(stone*2024, blink-1)
        cache[key] = calc
        return calc

total = 0
for s in stones:
    total += calc_stone(s, blinks)
print(total)



