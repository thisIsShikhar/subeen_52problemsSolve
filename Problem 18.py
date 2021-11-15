x=int(input())

if x>=1 and x<=100:
    for y in range(0,x):
        a = input().lower()
        z=[]
        y=[]
        for i in a:
            if i == " ":
                continue
            elif i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                z.append(i)
            else: y.append(i)
        print(*z,sep='')
        print(*y,sep='')
