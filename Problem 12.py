x=int(input())

if x>=0 and x<=100:
    for y in range(x):
        a= int(input())
        if a==0:
            print(0)
        elif a>=1 and a<=100:    
            for i in range(a-1,1,-1):
                a=a*i
            c=[int(x) for x in str(a)]
            b=0
            c.reverse()
            for y in c:
                if y ==0:
                    b+=1
                elif y!=0:
                    break
            print(b)