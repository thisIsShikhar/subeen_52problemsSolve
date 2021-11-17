T = int(input())

if 1 <= T <= 10:
    for i in range(T):
        N = int(input())
        if 2 <= N <= 1000000000000:
            flag = False
            for j in range(2, N):
                if N % j == 0:
                    flag = True
                    break
            if flag:
                print(f"{N} is not a prime")
            else:
                print(f"{N} is a prime")
