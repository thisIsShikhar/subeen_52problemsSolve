x = int(input())
if 1 <= x <= 100:
    for y in range(0, x):
        a = []
        srange = int(input())
        erange = int(input())
        for m in range(srange, erange+1):
            if m == 2:
                a.append(m)
            elif m>2:
                for i in range(2, m):
                    if m % i == 0:
                        break
                else:
                    a.append(m)

        print(len(a))
