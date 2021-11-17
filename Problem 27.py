T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        n = int(input())
        if 100<=n<=999:
            b= 0
            for j in str(n):
                b+=int(j)**3
            if b == n:
                print(f"{n} is an armstrong number!")
            else:
                print(f"{n} is not an armstrong number!")
