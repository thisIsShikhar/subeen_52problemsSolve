x=int(input())
v=0
if x>=1 and x<=100:
    for y in range(0,x):
        a = input().split(' ')
        z=0
        if (len(a))<=10000:
            for i in a:
                z+=1
        print(f"Count = {z}")
