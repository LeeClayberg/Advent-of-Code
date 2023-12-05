with open("files/day05.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    seeds = [int(num) for num in lines[0].split(' ')[1:]]
    ranges = [(seeds[i * 2], seeds[i * 2]+seeds[i * 2 + 1]) for i in range(0, len(seeds) // 2)]

    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []

    starting = None
    for i, line in enumerate(lines[2:]):
        if 'map' in line or '' == line:
            continue
        dest, source, length = [int(num) for num in line.split(' ')]
        if starting is None:
            starting = min(dest, source)
        else:
            starting = min(dest, source, starting)
        #start, change, max
        data = (dest, source - dest, dest + length)
        if i < 21:
            seed_soil.append(data)
        elif i < 49:
            soil_fertilizer.append(data)
        elif i < 98:
            fertilizer_water.append(data)
        elif i < 108:
            water_light.append(data)
        elif i < 125:
            light_temperature.append(data)
        elif i < 167:
            temperature_humidity.append(data)
        else:
            humidity_location.append(data)

    layers = list(reversed([seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location]))

    i = starting
    while True:
        # stuff
        current = i
        index = 0
        while index < len(layers):
            for node in layers[index]:
                if node[0] <= current < node[2]:
                    current += node[1]
                    break
            index += 1
        # check seed
        for seed_pair in ranges:
            if seed_pair[0] <= current < seed_pair[1]:
                print(i)
                exit()
        i += 1



