import math

x=int(input())

if x>=1 and x<=100:
    for y in range(0,x):
        a=int(input())
        if round(a)% math.sqrt(a)==0:
            print("YES")
        else: print("NO")
