
# Read in stuff
with open("files/day07.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]
    equations = [(int(line.split(': ')[0]), [int(n) for n in line.split(': ')[1].split(' ')]) for line in lines]

total = 0
for cal, nums in equations:
    answers = {nums[0]}
    for num in nums[1:]:
        answers = {answer + num for answer in answers}\
            .union({answer * num for answer in answers})\
            .union({int(f"{answer}{num}") for answer in answers})
    if cal in answers:
        total += cal
print(total)
