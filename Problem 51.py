T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        s1 = input('')
        s2 = input('')
        if len(s1)<128 and len(s2)<128:
            print(s1.find(s2))