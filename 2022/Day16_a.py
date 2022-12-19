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
    memo[key] = dict()
    for i in range(32):
        memo[key][i] = dict()


def max_path(current, minute, valves):
    maxes = []
    for nex in tunnels[current]:
        if minute + 1 <= 30:
            key_valves = frozenset(valves)
            if key_valves not in memo[nex][minute + 1].keys():
                memo[nex][minute + 1][key_valves] = max_path(nex, minute+1, valves)
            maxes.append(memo[nex][minute + 1][key_valves])
        if minute + 2 <= 30 and current not in valves and flows[current] != 0:
            calc_flow = flows[current] * (30 - minute - 1)
            new_valves = valves.copy()
            new_valves.add(current)
            key_valves = frozenset(new_valves)
            if key_valves not in memo[nex][minute + 2].keys():
                memo[nex][minute + 2][key_valves] = max_path(nex, minute+2, new_valves)
            maxes.append(memo[nex][minute + 2][key_valves] + calc_flow)
    return max(maxes) if len(maxes) > 0 else 0


answer = max_path('AA', 0, set())
print(answer)
