data = open('1.txt').read().split('\n')

def fuel(mass):
    return max(mass//3 - 2, 0)

s = 0

for line in data:
    current = fuel(int(line))
    s += current

    while current > 0:
        current = fuel(int(current))
        s += current

print(s)
