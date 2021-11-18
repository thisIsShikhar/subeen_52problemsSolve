import math
T = int(input())

if 1 <= T <= 1000:
    for i in range(T):
        a = int(input())
        b = int(input())
        c = int(input())
        s=(a+b+c)/2
        eq = (s*(s-a)*(s-b)*(s-c))
        area = math.sqrt(eq)
        area_float = "{:.3f}".format(area)
        print(f"Area = {area_float}")