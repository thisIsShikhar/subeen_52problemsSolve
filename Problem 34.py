T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        A = int(input())
        B = int(input())
        C = int(input())
        if (1 <= A) and (B <= 10 ** 9) and (C <= 10 ** 16):
            for x in range(1, C + 1):
                if x % A == 0 and x % B == 0:
                    print(x)
