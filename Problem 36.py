T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        N = int(input())
        if N<=20:
            a = []
            for j in range(N):
                S = input('')
                a.append(S)
            a.sort()
            print(a)