
with open("files/day22.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

block_ends = [(line.split('~')[0].split(','), line.split('~')[1].split(',')) for line in lines]

# Get all cubes in blocks
blocks = []
for start, end in block_ends:
    x1, y1, z1 = int(start[0]), int(start[1]), int(start[2])
    x2, y2, z2 = int(end[0]), int(end[1]), int(end[2])

    block = set()
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            for z in range(min(z1, z2), max(z1, z2)+1):
                block.add((x, y, z))
    blocks.append(block)

blocks.sort(key=(lambda blo: sorted([cube[2] for cube in blo])))

# Bring blocks down as far as they will go
supporting = {}
supported_by = {}
for b in range(0, len(blocks)):
    while True:
        block = blocks[b]
        # On the ground
        lowest = min(block, key=(lambda cube: cube[2]))
        if lowest[2] == 1:
            break

        # Hit other block
        translation = {(cube[0], cube[1], cube[2]-1) for cube in block}
        supported = False
        for s, support_block in enumerate(blocks[:b]):
            if len(support_block.intersection(translation)) > 0:
                if b not in supported_by:
                    supported_by[b] = set()
                supported_by[b].add(s)
                if s not in supporting:
                    supporting[s] = set()
                supporting[s].add(b)
                supported = True
        if supported:
            break
        blocks[b] = translation

# Check if able to be disintegrated
count = 0
for b in range(0, len(blocks)):
    if b in supporting:
        if all([len(supported_by[sup]) > 1 for sup in supporting[b]]):
            count += 1
    else:
        count += 1
print(count)