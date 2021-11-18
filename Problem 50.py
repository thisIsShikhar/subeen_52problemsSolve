T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        a = input('')
        b = list(a)
        c = []
        if len(a) <= 50:
            d = 0
            for j in b:
                # print(j)
                if j == 'L':
                    c.append(b[d - 1])
                elif j == 'R':
                    c.append(b[d + 1])
                else:
                    c.append(j)
                d += 1
            print(*c, sep='')
