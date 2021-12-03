lines = []

# Read in stuff
with open("files/input_21.txt", "r") as file_stream:
    while True:
        line = file_stream.readline()
        if not line:
            break
        lines.append(line[:-1])

# Parse data
ingredients = []
allergens = []
for line in lines:
    split = line.split(" (contains ")
    ingredients.append(split[0].split(" "))
    allergens.append(split[1][:-1].split(", "))

allergens_to_check = list(set([item for sublist in allergens for item in sublist]))

# Get possible ingredient possibilities
possibilities = []
for allergen in allergens_to_check:
    idxs = []
    for i in range(len(allergens)):
        if allergen in allergens[i]:
            idxs.append(i)
    options = set(ingredients[idxs[0]])
    for j in idxs[1:]:
        options = options.intersection(set(ingredients[j]))
    possibilities.append(list(options))

# Narrow possibilities
answers = dict()
while len(answers.keys()) != len(allergens_to_check):
    for idx, poss in enumerate(possibilities):
        if len(poss) == 1 and allergens_to_check[idx] not in answers.keys():
            answers[allergens_to_check[idx]] = poss[0]
    for i in range(len(possibilities)):
        possibilities[i] = list(set(possibilities[i]).difference(set(answers.values())))

# Find occurances
total= 0
for ingredient_ls in ingredients:
    total += len(set(ingredient_ls).difference(set(answers.values())))
print(total)
