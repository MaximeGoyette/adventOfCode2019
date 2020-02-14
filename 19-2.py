import math
from progressbar import progressbar
from machine import IntcodeMachine

program = open('19.txt').read()


def get_value(x, y):
    machine = IntcodeMachine(program)
    machine.inputs = [x, y]
    machine.run()
    return machine.outputs.pop(0)

def red(text):
    return '\033[91m' + text + '\033[0m'

def x1(y):
    return math.floor(y*(5/9)) + 1

def x2(y):
    return math.floor(y*(7/10))

def find_first(line):
    for i, x in enumerate(line):
        if x == '#':
            return i
    return 0

def find_last(line):
    for i, x in enumerate(line[::-1]):
        if x == '#':
            return i
    return 0

def other_coord(p, size=4):
    x, y = p
    return x + (size - 1), y - (size - 1)


y = 0
coords = set()
grid = []
bottom_left = None
top_right = None

while True:
    line = []
    a = x1(y)
    b = x2(y)
    for x in range(a, b + 1):
        line.append('#' if get_value(x, y) == 1 else '.')
    #grid.append(['.']*(a) + line)
    first, last = a + find_first(line) + 1, b - find_last(line) + 1
    coords.add((first, y))
    coords.add((last, y))
    other = other_coord((first, y), size=100)
    if other in coords:
        bottom_left = (first, y)
        top_right = other
        break
    y += 1

print((bottom_left[0] - 1)*10000 + top_right[1])
