from machine import IntcodeMachine

program = open('13.txt').read()

objects = [' ', '#', '□', '▬', 'o']

w, h = 46, 26 # educated guess

machine = IntcodeMachine(program)
machine.a[0] = 2 # put the coins in
machine.run()

def draw(screen):
    global objects
    lines = []
    for y in range(h):
        line = []
        for x in range(w):
            line.append(objects[screen.get((x, y), 0)])
        lines.append(''.join(line))
    print('\n'.join(lines))


def analyse(screen):
    ball_x = paddle_x = None
    number_of_blocks = 0

    for (x, y), o in screen.items():
        if o == 4:
            ball_x = x
        elif o == 3:
            paddle_x = x
        elif o == 2:
            number_of_blocks += 1
    return ball_x, paddle_x, number_of_blocks


number_of_blocks = None

while number_of_blocks is None or number_of_blocks > 0:
    screen = {}

    for i in range(0, len(machine.outputs), 3):
        x, y, o = machine.outputs[i:i+3]
        screen[(x, y)] = o

    ball_x, paddle_x, number_of_blocks = analyse(screen)

    if paddle_x < ball_x:
        next_move = 1
    elif paddle_x > ball_x:
        next_move = -1
    else:
        next_move = 0

    draw(screen)
    machine.inputs.append(next_move)
    machine.run()

print(f'Final score: {screen[(-1, 0)]}')
