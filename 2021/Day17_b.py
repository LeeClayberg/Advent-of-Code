
# Values from input for target area
x_min, x_max = 253, 280
y_min, y_max = -73, -46

y_vel_min, y_vel_max = y_min, (0 - y_min - 1)

increase = 1
cnt = 0
while cnt < x_min:
    cnt += increase
    increase += 1
x_vel_min = increase - 1
x_vel_max = x_max

count = 0
for y in range(y_vel_min, y_vel_max+1):
    for x in range(x_vel_min, x_vel_max+1):
        pos_x, pos_y = 0, 0
        vel_x, vel_y = x, y
        while pos_x < x_min or pos_y > y_max:
            pos_x += vel_x
            pos_y += vel_y
            vel_x = max(0, vel_x - 1)
            vel_y -= 1
        if pos_x in range(x_min, x_max+1) and pos_y in range(y_min, y_max+1):
            count += 1
print(count)
