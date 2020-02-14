data = open('1.txt').read().split('\n')

def fuel(mass):
    return max(mass//3 - 2, 0)

s = 0

for line in data:
    s += fuel(int(line))

print(s)
