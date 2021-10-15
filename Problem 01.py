a= int(input())

for b in range(0,a):
    c=int(input())
    if c>=0 and c<=2147483647:
        if c%2==0:
            print('even')
        else: print("odd")