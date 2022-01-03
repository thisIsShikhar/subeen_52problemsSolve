T = int(input())
if T <= 100:
    for i in range(1, T + 1):
        x = input()
        a = x.split(' ')

        p = int(a[0])
        q = int(a[1])
        c = int(a[2])
        print(p, q, c)

        eq = (p**q)%c
        print(f"Result = {eq}")
