class IntcodeMachine:
    def __init__(self, program, inputs=[]):
        self.program = program
        self.inputs = inputs
        self.outputs = []
        self.i = 0
        self.is_running = True
        self.relative_base = 0
        self.a = {i:int(value) for i, value in enumerate(program.split(','))}
        self.log = False

    def get_value(self, index):
        return self.a.get(index, 0)

    # 1
    def add(self, args):
        opt, p1, p2, p3 = args[:4]
        params = str(opt)[:-2].zfill(3)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        p2 = self.get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else self.get_value(p2 + self.relative_base)
        p3 = p3 if params[-3] == '0' else p3 + self.relative_base
        if self.log:
            print(f'Adds {p1} and {p2} and stores it at address {p3}.')
        self.a[p3] = p1 + p2
        self.i += 4

    # 2
    def mult(self, args):
        opt, p1, p2, p3 = args[:4]
        params = str(opt)[:-2].zfill(3)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        p2 = self.get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else self.get_value(p2 + self.relative_base)
        p3 = p3 if params[-3] == '0' else p3 + self.relative_base
        if self.log:
            print(f'Multiplies {p1} and {p2} and stores it at address {p3}.')
        self.a[p3] = p1 * p2
        self.i += 4

    # 3
    def store_at(self, args):
        opt, p1 = args[:2]
        params = str(opt)[:-2].zfill(3)
        p1 = p1 if params[-1] == '0' else p1 + self.relative_base
        try:
            value = self.inputs.pop(0)
            if self.log:
                print(f'Stores input ({value}) at address {p1}.')
            self.a[p1] = value
            self.i += 2
        except:
            if self.log:
                print(f'No input available, going into sleep mode.')
            self.is_running = False

    # 4
    def output(self, args):
        opt, p1 = args[:2]
        params = str(opt)[:-2].zfill(2)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        if self.log:
            print(f'Stores output ({p1}).')
        self.outputs.append(p1)
        self.i += 2

    # 5
    def jump_if_true(self, args):
        opt, p1, p2 = args[:3]
        params = str(opt)[:-2].zfill(2)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        p2 = self.get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else self.get_value(p2 + self.relative_base)
        if p1 != 0:
            if self.log:
                print(f'Jumps to i={p2}.')
            self.i = p2
        else:
            self.i += 3

    # 6
    def jump_if_false(self, args):
        opt, p1, p2 = args[:3]
        params = str(opt)[:-2].zfill(2)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        p2 = self.get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else self.get_value(p2 + self.relative_base)
        if p1 == 0:
            if self.log:
                print(f'Jumps to i={p2}.')
            self.i = p2
        else:
            self.i += 3

    # 7
    def less_than(self, args):
        opt, p1, p2, p3 = args[:4]
        params = str(opt)[:-2].zfill(3)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        p2 = self.get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else self.get_value(p2 + self.relative_base)
        p3 = p3 if params[-3] == '0' else p3 + self.relative_base
        if p1 < p2:
            self.a[p3] = 1
            if self.log:
                print(f'Sets value at address {p3} to 1.')
        else:
            self.a[p3] = 0
        self.i += 4

    # 8
    def equals(self, args):
        opt, p1, p2, p3 = args[:4]
        params = str(opt)[:-2].zfill(3)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        p2 = self.get_value(p2) if params[-2] == '0' else p2 if params[-2] == '1' else self.get_value(p2 + self.relative_base)
        p3 = p3 if params[-3] == '0' else p3 + self.relative_base
        if p1 == p2:
            self.a[p3] = 1
            if self.log:
                print(f'Set value at address {p3} to 1.')
        else:
            self.a[p3] = 0
        self.i += 4

    # 9
    def relative_base_ajust(self, args):
        opt, p1 = args[:2]
        params = str(opt)[:-2].zfill(2)
        p1 = self.get_value(p1) if params[-1] == '0' else p1 if params[-1] == '1' else self.get_value(p1 + self.relative_base)
        self.relative_base += p1
        if self.log:
            print(f'Adds {p1} to relative base (now {self.relative_base}).')
        self.i += 2

    # 99
    def exit_loop(self, args):
        self.is_running = False
        if self.log:
            print(f'Exits program.')

    def get_code(self, optcode):
        codes = {
            1: (self.add, 4),
            2: (self.mult, 4),
            3: (self.store_at, 2),
            4: (self.output, 2),
            5: (self.jump_if_true, 3),
            6: (self.jump_if_false, 3),
            7: (self.less_than, 4),
            8: (self.equals, 4),
            9: (self.relative_base_ajust, 2),
            99: (self.exit_loop, 0),
        }
        return codes[optcode]

    def run(self, log=False):
        self.log = log
        self.is_running = True
        while self.is_running:
            optcode = int(str(self.get_value(self.i))[-2:])
            func, nb_args = self.get_code(optcode)
            func([self.get_value(self.i + j) for j in range(nb_args)])


program = open('11.txt').read()
machine = IntcodeMachine(program)

grid = {}
direction = 0
position = (0, 0)
movements = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def next_direction(code):
    global direction
    direction = (direction + (1 if code == 0 else -1))%4

def next_movement(code):
    global movements, direction
    next_direction(code)
    movement = movements[direction]
    return movement

def next_position(code):
    global position
    movement = next_movement(code)
    position = (position[0] + movement[0], position[1] + movement[1])

while True:
    try:
        current_color = grid.get(position, 0)
        machine.inputs.append(current_color)
        machine.run(log=False)
        next_color = machine.outputs.pop(0)
        code = machine.outputs.pop(0)
        grid[position] = next_color
        next_position(code)
    except:
        break

print(len(grid))
