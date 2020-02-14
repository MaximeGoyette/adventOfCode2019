a = list(map(int, open('5.txt').read().split(',')))
i = 0
inputs = [1]
is_running = True

def add(args):
    global a, i
    opt, p1, p2, p3 = args[:4]
    params = str(opt)[:-2].zfill(3)
    p1 = a[p1] if params[-1] == '0' else p1
    p2 = a[p2] if params[-2] == '0' else p2
    a[p3] = p1 + p2
    i += 4

def mult(args):
    global a, i
    opt, p1, p2, p3 = args[:4]
    params = str(opt)[:-2].zfill(3)
    p1 = a[p1] if params[-1] == '0' else p1
    p2 = a[p2] if params[-2] == '0' else p2
    a[p3] = p1 * p2
    i += 4

def store_at(args):
    global a, i, inputs
    opt, p1 = args[:2]
    a[p1] = inputs.pop(0)
    i += 2

def output(args):
    global i
    opt, p1 = args[:2]
    print('output:', a[p1])
    i += 2

def exit_loop(args):
    global is_running
    is_running = False

codes = {
    1: add,
    2: mult,
    3: store_at,
    4: output,
    99: exit_loop,
}

while is_running:
    optcode = int(str(a[i])[-2:])
    if optcode == 99:
        break
    if optcode in codes:
        codes[int(str(a[i])[-2:])]([a[i], a[i + 1], a[i + 2] , a[i + 3]])
