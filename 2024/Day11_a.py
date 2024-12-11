
# Read in stuff
with open("files/day11.txt", "r") as file_stream:
    line = file_stream.read()
    stones = [int(s) for s in line[:-1].split(' ')]
    blinks = 25

    for _ in range(0, blinks):
        i = 0
        while i < len(stones):
            curr_stone = stones[i]
            if curr_stone == 0:
                stones[i] = 1
            elif len(str(curr_stone)) % 2 == 0:
                str_stone = str(curr_stone)
                len_stone = len(str_stone)
                left, right = str_stone[:len_stone // 2], str_stone[len_stone // 2:]
                stones[i] = int(left)
                i += 1
                stones.insert(i, int(right))
            else:
                stones[i] *= 2024
            i += 1
    print(len(stones))



