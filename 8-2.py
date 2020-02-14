data = open('8.txt').read()

w, h = 25, 6

lines = [data[i:i+w] for i in range(0, len(data), w)]
layers = [lines[i:i+h] for i in range(0, len(lines), h)]

result = [[0 for x in range(w)] for y in range(h)]

def get_pixel(x, y):
    for l in layers:
        if l[y][x] == '2':
            continue
        else:
            return l[y][x]

for y in range(h):
    for x in range(w):
        result[y][x] = get_pixel(x, y)

for line in result:
    print(''.join(line).replace('0', ' ').replace('1', '#'))
