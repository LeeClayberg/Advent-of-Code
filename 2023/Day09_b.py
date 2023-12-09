
with open("files/day09.txt", "r") as file_stream:
    lines = file_stream.readlines()

total = 0
for a, line in enumerate(lines):
    nums = [int(num) for num in line.split()]

    first_values = []
    while not all(num == 0 for num in nums):
        first_values.append(nums[0])
        new_nums = []
        for i in range(0, len(nums) - 1):
            new_nums.append(nums[i+1] - nums[i])
        nums = new_nums

    prior_value = 0
    for value in reversed(first_values):
        prior_value = value - prior_value
    total += prior_value
print(total)



