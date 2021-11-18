T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        X = int(input())
        K = int(input())
        if X<=10 and K<=6:
            a=0
            for i in range(K+1):
                a= a + (X**i)
            print(f"Result = {a}")