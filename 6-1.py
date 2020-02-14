data = open('6.txt').read().split('\n')

orbits = {'COM': None}
total = 0

for x in data:
    a, b = x.split(')')
    orbits[b] = a

for k, v in orbits.items():
    while v:
        v = orbits[v]
        total += 1

print(total)
