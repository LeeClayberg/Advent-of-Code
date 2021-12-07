
with open("files/input_07.txt", "r") as file_stream:
    numbers = list(map(lambda x: int(x), file_stream.readline().split(",")))

avg = int(sum(numbers) / len(numbers))

fuel = 0
for number in numbers:
    fuel += int((abs(avg - number) * (abs(avg - number) + 1)) / 2)
print(fuel)
