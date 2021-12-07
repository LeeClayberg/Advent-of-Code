import math

with open("files/input_07.txt", "r") as file_stream:
    numbers = list(map(lambda x: int(x), file_stream.readline().split(",")))

middle = sorted(numbers)[499:501]

median = int(sum(middle) / 2)

fuel = 0
for number in numbers:
    fuel += abs(median - number)
print(fuel)
