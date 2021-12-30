T = int(input())

if T <= 100:
    for i in range(T):
        N = int(input())
        if N <= 50:
            a=0
            for j in range(N,1,-1):
                print(f"2^{j} ",end='+ ')
            print('2 + 1')