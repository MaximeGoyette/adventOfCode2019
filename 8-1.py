data = open('8.txt').read()

w, h = 25, 6

lines = [data[i:i+w] for i in range(0, len(data), w)]
layers = [''.join(lines[i:i+h]) for i in range(0, len(lines), h)]

min_zeros = None
layers_nb = None

for i, l in enumerate(layers):
    c = l.count('0')
    if min_zeros is None or c < min_zeros:
        min_zeros = c
        layers_nb = i

print(layers[layers_nb].count('1')*layers[layers_nb].count('2'))
