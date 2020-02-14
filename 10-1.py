data = open('10.txt').read().split('\n')

def distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

def condition(a, b, c):
    if a[0] == b[0] == c[0]:
        return True, 9999999
    if a[1] == b[1] == c[1]:
        return True, 0
    try:
        return (c[1] - b[1])/(c[0] - b[0]) == (b[1] - a[1])/(b[0] - a[0]), (c[1] - b[1])/(c[0] - b[0])
    except:
        return False, None

def count(ax, ay):
    global data
    positions = []
    c = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if (x, y) == (ax, ay):
                continue
            elif data[y][x] == '#':
                positions.append((x, y))

    for x, y in positions:
        if x == ax:
            v = (9999999, y < ay)
            if not v in c:
                c[v] = []
            c[v].append((x, y))
            continue
        if y == ay:
            v = (0.000001, x < ax)
            if not v in c:
                c[v] = []
            c[v].append((x, y))
            continue

        d = ((y - ay)/(x - ax), x < ax)
        if not d in c:
            c[d] = []
        c[d].append((x, y))

    return c


max_count = None
answer = None

for ay in range(len(data)):
    for ax in range(len(data[0])):
        if data[ay][ax] == '#':
            c = count(ax, ay)
            c = len(c)
            if max_count == None or c > max_count:
                max_count = c
                answer = (ax, ay)

print(max_count)
print(answer)
