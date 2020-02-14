from itertools import cycle
from progressbar import progressbar

data = open('16.txt').read()

def get_pattern(index):
    base = [0, 1, 0, -1]
    output = []
    for b in base:
        output.extend([b]*(index + 1))
    output_cycle = cycle(output)
    next(output_cycle)
    return output_cycle

def get_next_phase(phase):
    result = []
    for i in range(len(phase)):
        pattern = get_pattern(i)
        output = 0
        for d, p in zip(str(phase), pattern):
            d = int(d)
            output += d*p
        result.append(str(output)[-1])
    return ''.join(result)

phase = data

for _ in progressbar(range(100)):
    next_phase = get_next_phase(phase)
    phase = next_phase

print(phase[:8])
