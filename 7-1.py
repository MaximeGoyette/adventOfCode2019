from itertools import permutations
from progressbar import progressbar

a = open('7.txt').read()
a = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
a = list(map(int, a.split(',')))

max_value = 0
answer = None

for modes in progressbar(list(permutations(range(5, 10)))):
    previous_output = 0

    mode_index = -1

    while True:
        mode_index = (mode_index + 1)%5
        mode = modes[mode_index]

        inputs = [mode, previous_output]
        i = 0
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
            global i, previous_output
            opt, p1 = args[:2]
            previous_output = a[p1]
            i += 2

        def jump_if_true(args):
            global a, i
            opt, p1, p2 = args[:3]
            params = str(opt)[:-2].zfill(2)
            p1 = a[p1] if params[-1] == '0' else p1
            p2 = a[p2] if params[-2] == '0' else p2
            if p1 != 0:
                i = p2
            else:
                i += 3

        def jump_if_false(args):
            global a, i
            opt, p1, p2 = args[:3]
            params = str(opt)[:-2].zfill(2)
            p1 = a[p1] if params[-1] == '0' else p1
            p2 = a[p2] if params[-2] == '0' else p2
            if p1 == 0:
                i = p2
            else:
                i += 3

        def less_than(args):
            global a, i
            opt, p1, p2, p3 = args[:4]
            params = str(opt)[:-2].zfill(3)
            p1 = a[p1] if params[-1] == '0' else p1
            p2 = a[p2] if params[-2] == '0' else p2
            if p1 < p2:
                a[p3] = 1
            else:
                a[p3] = 0
            i += 4

        def equals(args):
            global a, i
            opt, p1, p2, p3 = args[:4]
            params = str(opt)[:-2].zfill(3)
            p1 = a[p1] if params[-1] == '0' else p1
            p2 = a[p2] if params[-2] == '0' else p2
            if p1 == p2:
                a[p3] = 1
            else:
                a[p3] = 0
            i += 4

        def exit_loop(args):
            global is_running
            is_running = False

        codes = {
            1: (add, 4),
            2: (mult, 4),
            3: (store_at, 2),
            4: (output, 2),
            5: (jump_if_true, 3),
            6: (jump_if_false, 3),
            7: (less_than, 4),
            8: (equals, 4),
            99: (exit_loop, 0),
        }

        while is_running:
            optcode = int(str(a[i])[-2:])
            print(optcode, abs(previous_output))
            if optcode in codes:
                codes[optcode][0](a[i:i+codes[optcode][1]])

        if previous_output > max_value:
            max_value = previous_output
            answer = modes

print(max_value)
print(modes)
