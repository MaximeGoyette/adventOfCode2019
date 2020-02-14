minimum, maximum = tuple(map(int, open('4.txt').read().split('-')))

def check_double(passwd):
    streak = 0
    max_streak = 0
    ch = passwd[0]

    for x in passwd:
        if x == ch:
            streak += 1
        else:
            if streak == 2:
                return True
            if streak > max_streak:
                max_streak = streak
            streak = 1
            ch = x

    if streak == 2:
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
    if increases(passwd) and check_double(passwd):
        count += 1

print(count)
