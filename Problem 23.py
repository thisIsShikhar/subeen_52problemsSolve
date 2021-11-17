import string
x= int(input())
if x>=1 and x<=100:
    for y in range(0,x):
        letters= string.ascii_uppercase
        S=input().upper()
        for x in S:
            a = 0
            m = []
            for i in letters:
                a+=1
                if i == x:
                    m.append(a)
            
            print(*m,end ='')
        print()    