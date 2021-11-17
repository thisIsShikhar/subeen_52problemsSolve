T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        N = int(input())
        a=[]
        if N<=(2**64)-1:
            for x in range(1,N):
                if N%x==0:
                    a.append(x)
                else: continue
            if sum(a)==N:
                print(f"YES, {N} is a perfect number!")
            else:
                print(f"No, {N} is not a perfect number!")
