x= int(input())
if x>=1 and x<=100:
    for y in range(0,x):
        S = input()[::-1]
        if len(S)<=1000:
            print(S)
