T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        n = int(input())
        a=[]
        if n<=20:
            for j in range(n):
                b= int(input())
                a.append(b)
            c = sorted(a)
            if a == c:
                print('YES')
            else:
                print('NO')