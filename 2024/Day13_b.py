import sympy as sm

# Read in stuff
with open("files/day13.txt", "r") as file_stream:
    data = file_stream.read()[:-1]
    machines = data.split('\n\n')

    total = 0
    for machine in machines:
        b1, b2, p = machine.split('\n')
        b1x, b1y = [int(n) for n in b1.split(': X+')[-1].split(', Y+')]
        b2x, b2y = [int(n) for n in b2.split(': X+')[-1].split(', Y+')]
        px, py = [int(n) + 10000000000000 for n in p.split(': X=')[-1].split(', Y=')]

        a, b = sm.symbols(['a', 'b'])
        sol = sm.solve([a * b1x + b * b2x - px, a * b1y + b * b2y - py], [a, b])
        sol_a, sol_b = sol[a], sol[b]

        if int(sol_a) != sol_a or int(sol_b) != sol_b:
            continue
        cost = sol_a * 3 + sol_b
        total += cost
    print(total)
