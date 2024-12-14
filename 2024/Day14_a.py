
# Read in stuff
with open("files/day14.txt", "r") as file_stream:
    lines = [line[:-1] for line in file_stream.readlines()]

    wide, tall = 101, 103

    robots = []
    for line in lines:
        position, velocity = line.split(' ')
        pxr, pyr = position.split(',')
        px, py = int(pxr[2:]), int(pyr)
        vxr, vyr = velocity.split(',')
        vx, vy = int(vxr[2:]), int(vyr)
        robots.append({'p': (px, py), 'v': (vx, vy)})

    # Update positions
    for _ in range(0, 100):
        for r in range(0, len(robots)):
            position, velocity = robots[r]['p'], robots[r]['v']
            new_x = (position[0] + velocity[0] + wide) % wide
            new_y = (position[1] + velocity[1] + tall) % tall
            robots[r]['p'] = (new_x, new_y)

    # counts = {}
    # for robot in robots:
    #     if robot['p'] not in counts:
    #         counts[robot['p']] = 0
    #     counts[robot['p']] += 1
    # s = '\n'.join([' '.join([(str(counts[(x, y)]) if (x, y) in counts else '.') for x in range(0, wide)]) for y in range(0, tall)])
    # print(s)

    # Find quadrants
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        left, top = robot['p'][0] < wide // 2, robot['p'][1] < tall // 2
        right, bottom = robot['p'][0] > wide // 2, robot['p'][1] > tall // 2
        if left and top:
            q1 += 1
        elif right and top:
            q2 += 1
        elif left and bottom:
            q3 += 1
        elif right and bottom:
            q4 += 1

    print(q1 * q2 * q3 * q4)



