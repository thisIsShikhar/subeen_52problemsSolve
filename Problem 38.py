T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        n = int(input())
        m = int(input())
        for j in range(n):
            for k in range(0, j + 1):
                print(m, end=" ")
            print()
        for j in reversed(range(n)):
            for k in range(0, j):
                print(m, end=" ")
            print()
