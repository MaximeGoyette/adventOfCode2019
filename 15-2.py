import time
from copy import deepcopy
from machine import IntcodeMachine

program = open('15.txt').read()

machine = IntcodeMachine(program)


start_position = (0, 0)
oxygen_position = None

opposite_movements = {
    1: 2,
    2: 1,
    3: 4,
    4: 3,
}
current_position = start_position

backtrack = []
walls = set()
dead_ends = set()
walkable = set({(0, 0)})
all_positions = set()

def draw(extra=set()):
    time.sleep(0.01)
    min_x = max_x = min_y = max_y = None

    for (x, y) in walls | set({current_position}):
        if min_x is None or x < min_x:
            min_x = x
        if max_x is None or x > max_x:
            max_x = x
        if min_y is None or y < min_y:
            min_y = y
        if max_y is None or y > max_y:
            max_y = y

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    offset_x = -min_x
    offset_y = -min_y

    lines = []

    for y in range(height):
        line = []
        for x in range(width):
            absolute_coord = (x - offset_x, y - offset_y)
            if absolute_coord == oxygen_position:
                line.append(green('O'))
            elif absolute_coord in extra:
                line.append(blue('O'))
            elif absolute_coord == current_position:
                line.append('o')
            elif absolute_coord in walls:
                line.append(red('#'))
            elif absolute_coord in dead_ends:
                line.append(red('.'))
            elif absolute_coord in walkable:
                line.append('.')
            else:
                line.append(yellow('#'))
        lines.append(''.join(line))
    print('\n'.join(lines + ['']))

def get_shortest_path(origin, target):
    global walkable
    next_to_check = [origin]
    seen_from = {origin: None}
    seen_depth = {origin: 0}
    depth = 1

    while next_to_check:
        to_check = deepcopy(next_to_check)
        next_to_check = []

        while to_check:
            pos = to_check.pop(0)
            cx, cy = pos

            if (cx, cy) == target:
                break

            for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                nx, ny = cx + dx, cy + dy
                if not (nx, ny) in seen_from and (nx, ny) in walkable:
                    next_to_check.append((nx, ny))
                    seen_from[(nx, ny)] = (cx, cy)
                    seen_depth[(nx, ny)] = depth

        print(depth)
        draw(extra=set(seen_from.keys()))
        depth += 1

    path = []
    previous_position = target
    while previous_position:
        path.append(previous_position)
        previous_position = seen_from[previous_position]

    max_depth = None
    for (x, y), depth in seen_depth.items():
        if max_depth is None or depth > max_depth:
            max_depth = depth
    return path[::-1][1:], max_depth

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def blue(value):
    return '\033[94m' + value + '\033[0m'
def red(value):
    return '\033[91m' + value + '\033[0m'
def green(value):
    return '\033[92m' + value + '\033[0m'
def yellow(value):
    return '\033[93m' + value + '\033[0m'

while True:
    blocked_paths = set()
    has_moved = False
    for i, (dx, dy) in enumerate([(0, -1), (0, 1), (-1, 0), (1, 0)]):
        next_position = add(current_position, (dx, dy))
        all_positions.add(next_position)
        if has_moved:
            continue
        if next_position in walls | dead_ends or (backtrack and next_position == backtrack[-1][0]):
            blocked_paths.add(next_position)
            continue
        machine.inputs.append(i + 1)
        output = machine.run().pop(0)
        if output == 2:
            oxygen_position = next_position
            current_position = next_position
            walkable.add(current_position)
            has_moved = True
            continue
        elif output == 1:
            backtrack.append((current_position, opposite_movements[i + 1]))
            current_position = next_position
            walkable.add(current_position)
            has_moved = True
            continue
        elif output == 0:
            walls.add(next_position)
            continue

    if len(blocked_paths) == 4:
        dead_ends.add(current_position)
        next_position, movement = backtrack.pop(-1)
        machine.inputs.append(movement)
        output = machine.run().pop(0)
        if not output == 1:
            break
        current_position = next_position

    draw()

path, max_depth = get_shortest_path(oxygen_position, None)
print(max_depth)
