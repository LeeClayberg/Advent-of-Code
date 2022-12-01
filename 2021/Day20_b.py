import ast
import math

input = []
# Read in stuff
with open("files/input_20.txt", "r") as file_stream:
    algorithm = file_stream.readline()
    file_stream.readline()
    while True:
        line = file_stream.readline()
        if not line:
            break
        input.append(line[:-1])


def extend_image(image, amount):
    # top and bottom
    width = len(image[0])
    top_bottom = ''.join(["." for _ in range(width)])
    new_image = [top_bottom for _ in range(amount)] + image + [top_bottom for _ in range(amount)]
    for i in range(len(new_image)):
        new_image[i] = ''.join(["." for _ in range(amount)]) + new_image[i] + ''.join(["." for _ in range(amount)])
    return new_image


def shrink_image(image, amount):
    new_image = image[amount:-amount]
    for i in range(len(new_image)):
        new_image[i] = new_image[i][amount:-amount]
    return new_image


ex_image = extend_image(input, 20)
parts = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
for loop in range(50):
    final_image = []
    for a in range(len(ex_image) - 2):
        row = []
        for b in range(len(ex_image[a]) - 2):
            number = int(''.join(map(lambda offset: "0" if ex_image[a+offset[1]][b+offset[0]] == '.' else "1", parts)), 2)
            row.append(algorithm[number])
        final_image.append(''.join(row))
    if loop < 48:
        ex_image = extend_image(final_image, 20)
    else:
        ex_image = shrink_image(final_image, 2)
total_lights = ''.join(ex_image).count("#")
print(total_lights)
