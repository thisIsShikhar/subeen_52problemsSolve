T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        N = int(input())
        a = []
        for j in range(N - 1):
            l = int(input())
            if l <= N:
                a.append(l)
        for k in range(1, N + 1):
            if k not in a:
                print(k)
