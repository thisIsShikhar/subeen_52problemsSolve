a= int(input())

for b in range(0,a):
    c=int(input())
    if c>=0 and len(str(c))<=100:
        if c%2==0:
            print('even')
        else: print("odd")