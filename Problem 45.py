from math import factorial

T = int(input())
if T <= 100000:
    for x in range(1, T + 1):

        N = int(input())
        if N <= 50:
            for i in range(N+1):
                for j in range(i + 1):
                    print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
                print()
