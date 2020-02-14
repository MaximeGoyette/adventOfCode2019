from machine import IntcodeMachine

program = open('13.txt').read()

machine = IntcodeMachine(program)
machine.run()

print([x for x in machine.outputs[2::3]].count(2))
