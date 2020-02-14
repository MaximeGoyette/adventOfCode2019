minimum, maximum = tuple(map(int, open('4.txt').read().split('-')))

def check_double(passwd):
    for y in range(len(passwd) - 1):
        if passwd[y] == passwd[y + 1]:
            return True
    return False

def increases(passwd):
    current_max = 0
    for x in passwd:
        x = int(x)
        if x >= current_max:
            current_max = x
            continue
        else:
            return False
    return True


count = 0

for i in range(minimum, maximum):
    passwd = str(i)
    if check_double(passwd) and increases(passwd):
        count += 1

print(count)
