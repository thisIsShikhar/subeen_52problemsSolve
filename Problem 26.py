T = int(input())

if 1 <= T <= 1000:
    for i in range(T):
        X = float(input())
        a = 0
        if 0.0 <= X <= 100000.0:
            while X >= 1:
                X = X / 2
                a += 1
        print(f"{a} days")
