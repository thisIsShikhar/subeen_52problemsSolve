x=int(input())
v=0
if x>=1 and x<=100:
    for y in range(0,x):
        S = input().split(' ')
        z=0
        if (len(S))<=10000:
            for i in S:
                z+=1
        print(f"Count = {z}")
