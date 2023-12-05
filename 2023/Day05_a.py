with open("files/day05.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

    seeds = [int(num) for num in lines[0].split(' ')[1:]]

    seed_soil = []
    soil_fertilizer = []
    fertilizer_water = []
    water_light = []
    light_temperature = []
    temperature_humidity = []
    humidity_location = []

    for i, line in enumerate(lines[2:]):
        if 'map' in line or '' == line:
            continue
        dest, source, length = [int(num) for num in line.split(' ')]
        #start, change, max
        data = (source, dest - source, source + length)
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

    layers = [seed_soil, soil_fertilizer, fertilizer_water, water_light, light_temperature, temperature_humidity, humidity_location]

destinations = []
for seed in seeds:
    current = seed
    index = 0
    while index < len(layers):
        for node in layers[index]:
            if node[0] <= current < node[2]:
                current += node[1]
                break
        index += 1
    destinations.append(current)
print(min(destinations))
