a = list(map(int,open('2.txt').read().split(',')))

def add(p1, p2, p3):
    global a
    a[p3] = a[p1] + a[p2]

def mult(p1, p2, p3):
    global a
    a[p3] = a[p1] * a[p2]

codes = {
    1: add,
    2: mult,
}


i = 0

a[0] = 12
a[1] = 2

while i < len(a):
    if a[i] == 99:
        break
    if a[i] in codes:
        codes[a[i]](a[i + 1], a[i +2] , a[i +3] )
        i += 3
    i += 1

print(a[0])
