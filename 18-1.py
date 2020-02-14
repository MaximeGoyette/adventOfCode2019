from itertools import combinations, product

grid = '''#################
#i.G..c...e..H.p#
########.########
#j.A..b...f..D.o#
########@########
#k.E..a...g..B.n#
########.########
#l.F..d...h..C.m#
#################'''.split('\n')
#grid = open('18.txt').read().split('\n')

key_possible_values = 'abcdefghijklmnopqrstuvwxyz'
door_possible_values = set(key_possible_values.upper())
key_possible_values = set(key_possible_values)

def get_positions(grid):
    global key_possible_values, door_possible_values
    keys = {}
    doors = {}
    start_pos = None
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell in key_possible_values:
                keys[cell] = (x, y)
            elif cell == '@':
                start_pos = (x, y)
            elif cell in door_possible_values:
                doors[cell] = (x, y)
    return keys, doors, start_pos

class State:
    def __init__(self, owned_keys, steps, pos, depth):
        self.owned_keys = owned_keys
        self.steps = steps
        self.pos = pos
        self.depth = depth

def get_path(target, seen_from):
    path = []
    while target:
        path.append(target)
        target = seen_from[target]
    return path[::-1][1:]

def is_pos_in_grid(grid, x, y):
    return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

def scan(grid, state, unwalkable=set()):
    global owned_keys

    unwalkable.add('#')

    to_check = [state.pos]
    seen_from = {state.pos: None}

    reachable_keys = {}
    reachable_doors = {}

    while to_check:
        cx, cy = to_check.pop(0)

        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            cell = grid[ny][nx]
            if not (nx, ny) in seen_from and is_pos_in_grid(grid, nx, ny):
                if cell in (key_possible_values - state.owned_keys):
                    reachable_keys[cell] = (nx, ny)
                    seen_from[(nx, ny)] = (cx, cy)
                elif cell not in unwalkable:
                    to_check.append((nx, ny))
                    seen_from[(nx, ny)] = (cx, cy)

    reachable_keys = {k: get_path(v, seen_from) for k, v in reachable_keys.items()}

    return reachable_keys

def shortest_path(origin, target, unwalkable=set()):
    global grid

    unwalkable.add('#')

    to_check = [origin]
    seen_from = {origin: None}

    while to_check:
        cx, cy = to_check.pop(0)

        if (cx, cy) == target:
            break

        for (dx, dy) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = cx + dx, cy + dy
            cell = grid[ny][nx]
            if not (nx, ny) in seen_from and is_pos_in_grid(grid, nx, ny) and cell not in unwalkable:
                to_check.append((nx, ny))
                seen_from[(nx, ny)] = (cx, cy)

    return get_path(target, seen_from)

def get_doors_for_keys(keys):
    return {k.upper() for k in keys}

def get_path_between_keys(keys_on_grid, start_pos):
    paths = {}
    grid_items = list(keys_on_grid.items()) + [('@', start_pos)]

    for keys in combinations(grid_items, r=2):
        (key1, key1_pos), (key2, key2_pos) = keys
        if key1 == key2:
            continue
        path = set(shortest_path(key1_pos, key2_pos))
        paths[(key1, key2)] = path
        paths[(key2, key1)] = path

    return paths

keys_on_grid, doors_on_grid, start_pos = get_positions(grid)
min_steps = None
state_by_depth = {}
path_between_keys = get_path_between_keys(keys_on_grid, start_pos)

def has_all_keys(state):
    global keys_on_grid
    return state.owned_keys == keys_on_grid.keys()

def get_reachable_keys(state):
    global path_between_keys, keys_on_grid, doors_on_grid, grid

    missing_keys = keys_on_grid.keys() - state.owned_keys
    locked_doors = get_doors_for_keys(missing_keys)
    locked_doors_pos = {doors_on_grid[door] for door in locked_doors if door in doors_on_grid}

    reachable_keys = set()

    for missing_key in missing_keys:
        current_item = grid[state.pos[1]][state.pos[0]]
        path: set = path_between_keys.get((current_item, missing_key))
        if not path & locked_doors_pos:
            reachable_keys.add((missing_key, len(path)))

    return reachable_keys

def solve(state):
    if has_all_keys(state):
        global min_steps
        if min_steps is None or state.steps < min_steps:
            min_steps = state.steps
    else:
        global keys_on_grid
        reachable_keys = get_reachable_keys(state)
        for key, distance in reachable_keys:
            next_state = State(
                state.owned_keys | set([key]),
                state.steps + distance,
                keys_on_grid[key],
                state.depth + 1
            )
            solve(next_state)

original_state = State(set(), 0, start_pos, 0)
solve(original_state)

print(min_steps)
