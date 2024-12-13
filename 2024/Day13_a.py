
# Read in stuff
with open("files/day13.txt", "r") as file_stream:
    data = file_stream.read()[:-1]
    machines = data.split('\n\n')

    total = 0
    for machine in machines:
        b1, b2, p = machine.split('\n')
        b1x, b1y = [int(n) for n in b1.split(': X+')[-1].split(', Y+')]
        b2x, b2y = [int(n) for n in b2.split(': X+')[-1].split(', Y+')]
        px, py = [int(n) for n in p.split(': X=')[-1].split(', Y=')]
        eq1 = lambda a, b: a * b1x + b * b2x == px
        eq2 = lambda a, b: a * b1y + b * b2y == py

        lowest_cost = 100000000
        lowest_combo = None
        for press_a in range(0, 101):
            for press_b in range(0, 101):
                if eq1(press_a, press_b) and eq2(press_a, press_b):
                    cost = press_a * 3 + press_b
                    if cost < lowest_cost:
                        lowest_cost = cost
                        lowest_combo = (press_a, press_b)
        if lowest_combo is not None:
            total += lowest_cost
    print(total)

