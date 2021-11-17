T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        N = int(input())

        if N <= 40000000:
            for x in range(1,N+1):
                a = []
                for y in range(1,x):
                    if x%y == 0:
                        a.append(y)
                    else: continue
                if sum(a) == x:
                    print(x)
                else:
                    continue
