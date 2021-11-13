x=int(input())
v=0
if x>=1 and x<=100:
    for y in range(0,x):
        a = input()[::-1]
        b = a.split(' ')[::-1]
        if (len(a))<=1000:
            for n in b:
                print(n, end=' ')
            print()