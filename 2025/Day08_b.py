import math


def _straight_line_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(pow(x1-x2, 2) + pow(y1-y2, 2) + pow(z1-z2, 2))


# Read in stuff
with open("files/day08.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    points = [(int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])) for line in lines]

    # Create ordered segments
    used = set()
    closest = set()
    for point_1 in points:
        for point_2 in points:
            if point_1 == point_2:
                continue
            distance = _straight_line_distance(point_1, point_2)

            ordered = [point_1, point_2]
            ordered.sort()
            key = (ordered[0], ordered[1])
            if key in used:
                continue
            closest.add((ordered[0], ordered[1], distance))
            used.add(key)

    closest = list(closest)
    closest.sort(key=lambda p: p[2])

    circuits = []
    lookup_circuit = {}
    for point_1, point_2, dist in closest:
        in_1 = point_1 in lookup_circuit
        in_2 = point_2 in lookup_circuit
        if in_1 and in_2:
            if lookup_circuit[point_1] != lookup_circuit[point_2]:
                two_idx = circuits.index(lookup_circuit[point_2])
                for point in lookup_circuit[point_2]:
                    lookup_circuit[point_1].add(point)
                    lookup_circuit[point] = lookup_circuit[point_1]
                circuits.pop(two_idx)
        elif not in_1 and in_2:
            existing_circuit = lookup_circuit[point_2]
            existing_circuit.add(point_1)
            lookup_circuit[point_1] = existing_circuit
        elif in_1 and not in_2:
            existing_circuit = lookup_circuit[point_1]
            existing_circuit.add(point_2)
            lookup_circuit[point_2] = existing_circuit
        elif not in_1 and not in_2:
            new_circuit = {point_1, point_2}
            circuits.append(new_circuit)
            lookup_circuit[point_1] = new_circuit
            lookup_circuit[point_2] = new_circuit
        if len(circuits) == 1 and len(circuits[0]) == 1000:
            x1, x2 = point_1[0], point_2[0]
            print(x1 * x2)
            break








