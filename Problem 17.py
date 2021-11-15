x=int(input())
v=0
if x>=1 and x<=100:
    for y in range(0,x):
        a = input().lower()
        z=0
        if (len(a))<=1000:
            for i in a:
                if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                    z+=1
            print(f"Number of vowels = {z}")
