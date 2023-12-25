
with open("files/day24.txt", "r") as file_stream:
    lines = file_stream.readlines()
    lines = [line[:-1] for line in lines]

trajectories = []
for line in lines:
    point, velocity = line.split(' @ ')
    px, py, _ = point.split(', ')
    vx, vy, _ = velocity.split(', ')
    px, py, _ = int(px), int(py), _
    vx, vy, _ = int(vx), int(vy), _

    m = vy / vx
    b = py - m * px
    trajectories.append((m, b, px, py, vx, vy))

range_start = 200000000000000
range_end = 400000000000000
checked = set()
total = 0
for a, t1 in enumerate(trajectories):
    for b, t2 in enumerate(trajectories):
        if t1 == t2:
            continue
        if t1[0] == t2[0]:
            continue
        pair = (min(t1, t2), max(t1, t2))
        if pair in checked:
            continue
        checked.add(pair)

        int_x = (t2[1] - t1[1]) / (t1[0] - t2[0])
        int_y = int_x * t1[0] + t1[1]

        t1_check_1 = int_x < t1[2] if t1[4] < 0 else int_x > t1[2]
        t1_check_2 = int_y < t1[3] if t1[5] < 0 else int_y > t1[3]

        t2_check_1 = int_x < t2[2] if t2[4] < 0 else int_x > t2[2]
        t2_check_2 = int_y < t2[3] if t2[5] < 0 else int_y > t2[3]
        print((t1[2], t1[3]), (t2[2], t2[3]), (int_x, int_y))

        if range_start <= int_x <= range_end and range_start <= int_y <= range_end and t1_check_1 and t1_check_2 and t2_check_1 and t2_check_2:
            total += 1
            print('here')

print(total)



