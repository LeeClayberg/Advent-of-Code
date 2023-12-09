
with open("files/day09.txt", "r") as file_stream:
    lines = file_stream.readlines()

total = 0
for line in lines:
    nums = [int(num) for num in line.split()]

    last_values = []
    while not all(num == 0 for num in nums):
        last_values.append(nums[-1])
        new_nums = []
        for i in range(0, len(nums) - 1):
            new_nums.append(nums[i+1] - nums[i])
        nums = new_nums
    total += sum(last_values)
print(total)



