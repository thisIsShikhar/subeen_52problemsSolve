x=int(input())
if x>=1 and x<=100:
    for y in range(0,x):
        a=input().split(' ')
        z=[]
        for i in a:
            try:
                int(i)
                z.append(i)
            except:
                continue
        
        if len(z)>=1 and len(z)<=100 and sum(int(j) for j in z)<=10000000:
            print(z)
            print(len(z))