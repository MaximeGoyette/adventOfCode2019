from math import atan2, degrees

data = open('10.txt').read().split('\n')

def get_angles(ax, ay):
    global data
    relative_positions = []
    c = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) == (ax, ay):
                continue
            elif data[y][x] == '#':
                relative_positions.append((x - ax, y - ay))

    for x, y in relative_positions:
        delta = -degrees(atan2(y, x))
        distance = (x**2 + y**2)**0.5
        if not delta in c:
            c[delta] = []
        c[delta].append((distance, x, y))

    return c


max_count = None
best_position = None

for ay in range(len(data)):
    for ax in range(len(data[0])):
        if data[ay][ax] == '#':
            c = get_angles(ax, ay)
            c = len(c)
            if max_count == None or c > max_count:
                max_count = c
                best_position = (ax, ay)


c = get_angles(*best_position)
c = {k: sorted(v) for k, v in c.items()}


angles = sorted(c, reverse=True)
up_index = angles.index(90)
angles = angles[up_index:] + angles[:up_index]

asteroids_destroyed = []
i = 0

while True:
    destroyed_asteroid = None
    while not destroyed_asteroid:
        current_angle = angles[i%len(angles)]
        i += 1
        destroyed_asteroid = c[current_angle].pop(0) if len(c[current_angle]) > 0 else None
    asteroids_destroyed.append(destroyed_asteroid)

    if len(asteroids_destroyed) == 200:
        distance, x, y = asteroids_destroyed[199]
        print((x + best_position[0], y + best_position[1]))
        exit(0)
