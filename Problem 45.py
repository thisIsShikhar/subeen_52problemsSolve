from math import factorial

T = int(input())
if T <= 100000:
    for i in range(1, T + 1):

        N = int(input())
        if N <= 50:
            for i in range(N):
                for j in range(i + 1):
                    print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
                print()
