x=int(input())

if x>=0 and x<=100:
    for y in range(x):
        a= int(input())
        if a==0:
            print(1)
        elif a>=1 and a<=15:    
            for i in range(a-1,1,-1):
                a=a*i
            print(a)