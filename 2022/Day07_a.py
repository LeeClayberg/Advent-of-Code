file_system = dict()
current_spot = []
# Read in stuff
with open("files/input_07.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        parts = line[:-1].split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    current_spot = []
                elif parts[2] == "..":
                    current_spot = current_spot[:-1]
                else:
                    current_spot.append(parts[2])
            else:
                # List
                continue
        else:
            # Get to current spot
            current_ref = file_system
            for link in current_spot:
                current_ref = current_ref[link]
            if parts[0] == "dir":
                current_ref[parts[1]] = dict()
            else:
                current_ref[parts[1]] = int(parts[0])


# Calculations
def directory_sizes(system):
    if isinstance(system, int):
        return system
    else:
        counts = []
        new_count = 0
        for sub in system.keys():
            output = directory_sizes(system[sub])
            if isinstance(output, int):
                new_count += output
            else:
                counts.extend(output)
                new_count += output[-1]
        return counts + [new_count]


print(sum([dirt for dirt in directory_sizes(file_system) if dirt <= 100000]))
