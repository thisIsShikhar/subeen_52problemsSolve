x=int(input())
if x>=10000 and x<=99999:
    for y in range(0,x):
        a=input()
        print(f'Sum = {int(a[0])+int(a[-1])}')