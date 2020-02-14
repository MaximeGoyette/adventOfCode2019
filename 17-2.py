from machine import IntcodeMachine

program = open('17.txt').read()

machine = IntcodeMachine(program)
machine.a[0] = 2

outputs = '''#######...#####
#.....#...#...#
#.....#...#...#
......#...#...#
......#...###.#
......#.....#.#
^########...#.#
......#.#...#.#
......#########
........#...#..
....#########..
....#...#......
....#...#......
....#...#......
....#####......'''.split('\n')
outputs = ''.join([chr(code) for code in machine.run()]).split('\n')[:-3]

directions = ['>', 'v', '<', '^']

def get_intersections(outputs):
    intersections = set()
    for y in range(len(outputs)):
        for x in range(len(outputs[0])):
            if outputs[y][x] == '#':
                n = 0
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if 0 <= x + dx < len(outputs[0]) and 0 <= y + dy < len(outputs) and outputs[y + dy][x + dx] in ['#'] + directions:
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

def get_adjacents(outputs, x, y):
    adjacents = set()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= x + dx < len(outputs[0]) and 0 <= y + dy < len(outputs) and outputs[y + dy][x + dx] in ['#'] + directions:
            adjacents.add((x + dx, y + dy))
    return adjacents

def diff(a, b):
    return (b[0] - a[0], b[1] - a[1])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def get_next_direction(direction, adjacents, position, previous_position):
    if previous_position is not None:
        adjacents.remove(previous_position)
    next_position = list(adjacents)[0]
    dy, dx = diff(position, next_position)
    next_direction = directions.index(mov_to_dir[(dx, dy)])
    pivot = (next_direction - direction)%4
    return pivot, next_direction

intersections = get_intersections(outputs)
mov_to_dir = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, -1): '<',
    (0, 1): '>',
}
dir_to_mov = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}
pivots = {
    1: ['R'],
    3: ['L'],
}
position = None
previous_position = None
direction = None

for y, line in enumerate(outputs):
    for x, cell in enumerate(line):
        if cell in directions:
            position = (x, y)
            direction = directions.index(cell)

instructions = []
count = 0

while True:
    adjacents = get_adjacents(outputs, position[0], position[1])
    if previous_position is not None and len(adjacents) == 1:
        instructions.append(count)
        break
    elif len(adjacents) == 4:
        pass
    else:
        pivot, next_direction = get_next_direction(direction, adjacents, position, previous_position)
        next_instructions = pivots.get(pivot)
        if next_instructions:
            if count > 0:
                instructions.append(count)
            instructions.extend(next_instructions)
            count = 0
            direction = next_direction
    previous_position = position
    movement = dir_to_mov[directions[direction]]
    position = add(position, movement[::-1])
    count += 1

MAIN = 'A,A,C,B,C,B,C,B,C,A\n'
A = 'L,10,L,8,R,8,L,8,R,6\n'
B = 'R,6,R,6,L,8,L,10\n'
C = 'R,6,R,8,R,8\n'

def print_machine_output(outputs):
    print(''.join([chr(code) for code in outputs]))

print_machine_output(machine.outputs)
print(MAIN)
machine.inputs.extend([ord(c) for c in MAIN])
print_machine_output(machine.run())

print(A)
machine.inputs.extend([ord(c) for c in A])
print_machine_output(machine.run())

print(B)
machine.inputs.extend([ord(c) for c in B])
print_machine_output(machine.run())

print(C)
machine.inputs.extend([ord(c) for c in C])
print_machine_output(machine.run())

print('n\n')
machine.inputs.extend([ord(c) for c in 'n' + '\n'])
print(machine.run()[-1])
