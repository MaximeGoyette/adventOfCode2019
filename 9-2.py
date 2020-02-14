outputs = []
i = 0
is_running = True

inputs = [2]
relative_base = 0
program = open('9.txt').read()

a = {i:int(value) for i, value in enumerate(program.split(','))}
log = False

def get_value(index):
    return a.get(index, 0)

# 1
def add(args):
    global a, i
    opt, p1, p2, p3 = args[:4]
    params = str(opt)[:-2].zfill(3)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    p2 = get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else get_value(p2 + relative_base)
    p3 = p3 if params[-3] == '0' else p3 + relative_base
    if log:
        print(f'Adds {p1} and {p2} and stores it at address {p3}.')
    a[p3] = p1 + p2
    i += 4

# 2
def mult(args):
    global a, i
    opt, p1, p2, p3 = args[:4]
    params = str(opt)[:-2].zfill(3)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    p2 = get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else get_value(p2 + relative_base)
    p3 = p3 if params[-3] == '0' else p3 + relative_base
    if log:
        print(f'Multiplies {p1} and {p2} and stores it at address {p3}.')
    a[p3] = p1 * p2
    i += 4

# 3
def store_at(args):
    global a, i, inputs
    opt, p1 = args[:2]
    params = str(opt)[:-2].zfill(3)
    p1 = p1 if params[-1] == '0' else p1 + relative_base
    value = inputs.pop(0)
    if log:
        print(f'Stores input ({value}) at address {p1}.')
    a[p1] = value
    i += 2

# 4
def output(args):
    global i, previous_output
    opt, p1 = args[:2]
    params = str(opt)[:-2].zfill(2)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    if log:
        print(f'Stores output ({p1}).')
    outputs.append(p1)
    i += 2

# 5
def jump_if_true(args):
    global a, i
    opt, p1, p2 = args[:3]
    params = str(opt)[:-2].zfill(2)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    p2 = get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else get_value(p2 + relative_base)
    if p1 != 0:
        if log:
            print(f'Jumps to i={p2}.')
        i = p2
    else:
        i += 3

# 6
def jump_if_false(args):
    global a, i
    opt, p1, p2 = args[:3]
    params = str(opt)[:-2].zfill(2)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    p2 = get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else get_value(p2 + relative_base)
    if p1 == 0:
        if log:
            print(f'Jumps to i={p2}.')
        i = p2
    else:
        i += 3

# 7 21107
def less_than(args):
    global a, i
    opt, p1, p2, p3 = args[:4]
    params = str(opt)[:-2].zfill(3)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    p2 = get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else get_value(p2 + relative_base)
    p3 = p3 if params[-3] == '0' else p3 + relative_base
    if p1 < p2:
        a[p3] = 1
        if log:
            print(f'Sets value at address {p3} to 1.')
    else:
        a[p3] = 0
    i += 4

# 8
def equals(args):
    global a, i
    opt, p1, p2, p3 = args[:4]
    params = str(opt)[:-2].zfill(3)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    p2 = get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else get_value(p2 + relative_base)
    p3 = p3 if params[-3] == '0' else p3 + relative_base
    if p1 == p2:
        a[p3] = 1
        if log:
            print(f'Set value at address {p3} to 1.')
    else:
        a[p3] = 0
    i += 4

# 9
def relative_base_ajust(args):
    global a, i, relative_base
    opt, p1 = args[:2]
    params = str(opt)[:-2].zfill(2)
    p1 = get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else get_value(p1 + relative_base)
    relative_base += p1
    if log:
        print(f'Adds {p1} to relative base (now {relative_base}).')
    i += 2

# 99
def exit_loop(args):
    global is_running
    is_running = False
    if log:
        print(f'Exits program.')

codes = {
    1: (add, 4),
    2: (mult, 4),
    3: (store_at, 2),
    4: (output, 2),
    5: (jump_if_true, 3),
    6: (jump_if_false, 3),
    7: (less_than, 4),
    8: (equals, 4),
    9: (relative_base_ajust, 2),
    99: (exit_loop, 0),
}

while is_running:
    optcode = int(str(get_value(i))[-2:])
    if optcode in codes:
        codes[optcode][0]([get_value(i + j) for j in range(codes[optcode][1])])

print(f'Outputs: {outputs}')
