x = int(input())

if 1 <= x <= 100:
    for y in range(0, x):
        a = int(input())
        b = int(input())
        if a >= 1 and b <= 100000:
            if a > b:
                greater = a
            else:
                greater = b

            while True:
                if (greater % a == 0) and (greater % b == 0):
                    lcm = greater
                    break
                greater += 1

            print(f"LCM = {lcm}")
