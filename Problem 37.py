T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        N = int(input())
        if N <= 100000000:
            print(str(N)[::-1])
