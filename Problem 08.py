x=int(input())
v=0
if x>=1 and x<=100:
    for y in range(0,x):
        a=input().split(' ')
        z=[]
        v+=1
        for i in a:
            
            if (int(i))<=1000:
                try:
                    int(i)
                    z.append(int(i))
                except:
                    continue
        
        if len(z)==3:
            z.sort()
            print(f'Case {v}: {z[0]} {z[1]} {z[2]}')
        