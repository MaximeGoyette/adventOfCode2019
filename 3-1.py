a, b = open('3.txt').read().split('\n')

coords = {}

def execute(letter, movements):
    global coords
    current = (0, 0)

    for x in movements.split(','):
        if x[0] == 'R':
            for i in range(int(x[1:])):
                cc = (current[0] + i, current[1])
                if not cc in coords:
                    coords[cc] = set()
                coords[cc].add(letter)
            current = (current[0] + int(x[1:]), current[1])
        elif x[0] == 'L':
            for i in range(int(x[1:])):
                cc = (current[0] - i, current[1])
                if not cc in coords:
                    coords[cc] = set()
                coords[cc].add(letter)
            current = (current[0] - int(x[1:]), current[1])
        elif x[0] == 'U':
            for i in range(int(x[1:])):
                cc = (current[0], current[1] - i)
                if not cc in coords:
                    coords[cc] = set()
                coords[cc].add(letter)
            current = (current[0], current[1] - int(x[1:]))
        elif x[0] == 'D':
            for i in range(int(x[1:])):
                cc = (current[0], current[1] + i)
                if not cc in coords:
                    coords[cc] = set()
                coords[cc].add(letter)
            current = (current[0], current[1] + int(x[1:]))

execute('A', a)
execute('B', b)

coords.pop((0, 0), None)

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

min_dist = None
answer = None

for c in coords:
    if len(coords[c]) > 1:
        d = dist((0, 0), c)
        if answer == None or d < min_dist:
            min_dist = d
            answer = c

print(min_dist)
