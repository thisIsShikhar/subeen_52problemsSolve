x=int(input())
v=0
if x>=1 and x<=100:
    for y in range(0,x):
        a = input()
        c = [x for x in a]
        d = input()
        y=0
        for i in c:
            if i==d:
                y+=1
        if y>=1:
            print(f"Occurrence of '{d}' in '{a}' = {y}")
        else: print(f"'{d}' is not present")