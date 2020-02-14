data = open('6.txt').read().split('\n')

orbits = {'COM': None}

for x in data:
    a, b = x.split(')')
    orbits[b] = a

def get_path(start):
    global orbits
    path = []
    current = start
    while current:
        path.append(current)
        current = orbits[current]
    return path[1:]

p1 = get_path('YOU')
p2 = get_path('SAN')

while p1[-1] == p2[-1]:
    p1.pop(-1)
    p2.pop(-1)

print(len(p1) + len(p2))
