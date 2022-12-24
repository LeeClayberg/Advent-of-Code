flows = dict()
tunnels = dict()
with open("files/input_16.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        parts = line[:-1].split(" ")
        valve = parts[1]
        flow = int(parts[4][5:-1])
        options = line[:-1].split(", ")
        options[0] = options[0][-2:]

        flows[valve] = flow
        tunnels[valve] = options

memo = dict()
for key in flows.keys():
    for key2 in flows.keys():
        memo[(key, key2)] = dict()
        for i in range(32):
            for j in range(32):
                memo[(key, key2)][(i, j)] = dict()


def max_path(current, minute, valves):
    me, elephant = current
    min1, min2 = minute
    maxes = []
    for me_next in tunnels[me]:
        elephant_tunnels = [tun for tun in tunnels[elephant] if tun != me_next]


    return max(maxes) if len(maxes) > 0 else 0


answer = max_path(('AA', 'AA'), (0, 0), set())
print(answer)
