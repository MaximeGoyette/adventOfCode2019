from machine import IntcodeMachine

program = open('17.txt').read()

machine = IntcodeMachine(program)
outputs = ''.join([chr(code) for code in machine.run()]).split('\n')[:-2]

def get_intersections(outputs):
    intersections = set()
    for y in range(len(outputs)):
        for x in range(len(outputs[0])):
            if outputs[y][x] == '#':
                n = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= x + dx < len(outputs[0]) and 0 <= y + dy < len(outputs) and outputs[y + dy][x + dx] == '#':
                        n += 1
                if n == 4:
                    intersections.add((x, y))
    return intersections

def print_map(outputs):
    intersections = get_intersections(outputs)
    lines = []
    for y in range(len(outputs)):
        line = []
        for x in range(len(outputs[0])):
            if (x, y) in intersections:
                line.append('O')
            else:
                line.append(outputs[y][x])
        lines.append(''.join(line))
    print('\n'.join(lines))

total = 0
for x, y in get_intersections(outputs):
    total += x*y
print(total)
