from itertools import permutations
from machine import IntcodeMachine

program = open('7.txt').read()

max_output = None

for modes in permutations(range(5, 10)):
    output = 0
    machines = [IntcodeMachine(program, inputs=[mode]) for mode in modes]
    is_running = True
    while is_running:
        for machine in machines:
            machine.inputs.append(output)
            outputs = machine.run()
            if not outputs:
                is_running = False
                break
            output = outputs[0]
            if max_output is None or output > max_output:
                max_output = output
                print(max_output, modes)
