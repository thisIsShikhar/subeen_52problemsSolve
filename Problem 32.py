T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        X = int(input())
        N = int(input())
        if 1 <= X <= N <= 1000000:
            a = 0
            while True:
                a = a + X
                if a <= N:
                    print(a)
                else:
                    break
        else:
            print("Invalid!")
