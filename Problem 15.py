x=int(input())

if x>=1 and x<=100:
    for y in range(0,x):
        a = input()

        if len(a)<=1000:
            c = [x for x in a]
            m = dict((i, a.count(i)) for i in a)
            for k, v in m.items():
                print(f"{k} = {v}")

