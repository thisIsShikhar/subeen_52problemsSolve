x=int(input())
v=0
if x>=1 and x<=100:
    for y in range(0,x):
        a=input().split(' ')
        oprun= int(a[0])
        currun= int(a[1])
        ballrem= int(a[2])
        bowled = 300-ballrem
        currentrr= currun/(bowled/6)
        reqrr= ((oprun+1)-currun)/(ballrem/6)
        print(f'{currentrr:.2f} {reqrr:.2f}')