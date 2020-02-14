from itertools import cycle
from progressbar import progressbar


data = open('16.txt').read()*10000
data = '03036732577212944063491565474664'*10000

def get_pattern(index):
    base = [0, 1, 0, -1]
    output = []
    for b in base:
        output.extend([b]*(index + 1))
    return output[1:]

def get_next_phase(phase):
    result = []
    for i in progressbar(range(len(phase))):
        pattern = get_pattern(i)
        output = 0
        for d, p in zip(str(phase), pattern):
            d = int(d)
            output += d*p
        result.append(str(output)[-1])
    return ''.join(result)

phase = data

for _ in range(100):
    next_phase = get_next_phase(phase)
    phase = next_phase

offset = int(phase[:7])
message = phase[offset:offset + 8]

print(message)
