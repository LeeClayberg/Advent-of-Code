
# Read in stuff
with open("files/day24.txt", "r") as file_stream:
    # Setup
    values, gates = file_stream.read()[:-1].split('\n\n')

    # Find current values
    values = {key: bool(int(value)) for key, value in [row.split(': ') for row in values.split('\n')]}
    gates = [(v1, op, v2, out) for v1, op, v2, _, out in [gate.split(' ') for gate in gates.split('\n')]]

    x = sorted([key for key in values.keys() if key[0] == 'x'], reverse=True)
    x = int(''.join([('1' if values[key] else '0') for key in x]), 2)

    y = sorted([key for key in values.keys() if key[0] == 'y'], reverse=True)
    y = int(''.join([('1' if values[key] else '0') for key in y]), 2)

    answer = bin(x + y)[2:]
    for idx, value in enumerate(reversed(answer)):
        key = f"z{idx:02}"
        values[key] = (value == '1')

    while len(gates) > 0:
        v1, op, v2, out = gates.pop(0)
        if v1 not in values or v2 not in values:
            gates.append((v1, op, v2, out))
            continue
        print(op)
        if op == 'AND':
            values[out] = values[v1] and values[v2]
        elif op == 'OR':
            values[out] = values[v1] or values[v2]
        elif op == 'XOR':
            values[out] = values[v1] != values[v2]



