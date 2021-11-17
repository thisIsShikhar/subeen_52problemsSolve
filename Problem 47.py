T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        n1 = input().split(' ')
        n2 = input().split(' ')
        n3 = n1 + n2
        k=[]
        for item in n3:
            k.append(int(item))
        k.sort()
        k = list(dict.fromkeys(k))

        print(k, sep=' ')