import math

T = int(input())

if T <= 100:
    for i in range(T):
        n = int(input())
        if n <= 15:
            a = 0
            for j in range(1, n + 1):
                a += (j / math.factorial(j))

            print("{:.4f}".format(a))
