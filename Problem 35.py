T = int(input())
if 1 <= T <= 100:
    for i in range(1, T + 1):
        a = input()
        r = int(input())
        x = input()
        b = a.split(' ')
        c = x.split(' ')
        Xc = int(b[0])
        Yc = int(b[1])
        X = int(c[0])
        Y = int(c[1])

        if ((X - Xc) ** 2) + ((Y - Yc) ^ 2) < (r ** 2):
            print('The point is inside the circle')
        else:
            print('The point is not inside the circle')
