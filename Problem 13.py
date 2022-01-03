import math

T = int(input())
if 1 <= T <= 100:
    for i in range(1, T + 1):
        a = input()
        if len(a) <= 20:
            z = a.split()
            c = []
            d = 1
            for i in z:
                if i in c:
                    continue
                else:
                    count = z.count(i)
                    if count >= 2:
                        c.append(i)
                        d *= count

            print(f"1/{int(math.factorial(len(z))/d)}")
