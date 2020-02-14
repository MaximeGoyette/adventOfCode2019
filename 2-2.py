for x in range(100):
    for y in range(100):

        a = list(map(int,open('2.txt').read().split(',')))


        def add(p1, p2, p3):
            a[p3] = a[p1] + a[p2]

        def mult(p1, p2, p3):
            a[p3] = a[p1] * a[p2]

        codes = {
            1: add,
            2: mult,
        }


        i = 0

        a[1]= x
        a[2]= y

        while i < len(a):
            if a[i] == 99:
                break
            if a[i] in codes:
                codes[a[i]](a[i + 1], a[i +2] , a[i +3] )
                i += 3
            i += 1

        if a[0] == 19690720:
            print(x, y)
            exit()
