from machine import IntcodeMachine

program = open('19.txt').read()


def get_value(x, y):
    machine = IntcodeMachine(program)
    machine.inputs = [x, y]
    machine.run()
    return machine.outputs.pop(0)

output = []

for y in range(50):
    line = []
    for x in range(50):
        line.append(str(get_value(x, y)))
    output.append(''.join(line))

print('\n'.join(output).count('1'))
