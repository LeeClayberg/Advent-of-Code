import math

with open("files/day06.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]
    time = int(''.join(lines[0].split()[1:]))
    distance = int(''.join(lines[1].split()[1:]))

    # distance < x * (time - x)
    # 0 < -x^2 + (time)x - distance
    fx = lambda x: x * (time - x)
    a, b, c = -1, time, -distance
    fx1 = (-b + math.sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)
    fx2 = (-b - math.sqrt(pow(b, 2) - (4 * a * c))) / (2 * a)

    begin = math.ceil(min(fx1, fx2))
    end = math.floor(max(fx1, fx2))
    if fx(begin) == distance:
        begin += 1
    if fx(end) == distance:
        end -= 1

    print(end - begin + 1)
