T = int(input())

if 1 <= T <= 100:
    for y in range(0, T):
        a = input()
        b = input()
        if len(a) < 128 and len(b) < 128:
            def to_find(string, sub):
                count = 0
                start = 0
                while True:
                    start = string.find(sub, start) + 1
                    if start > 0:
                        count += 1
                    else:
                        return count


            print(to_find(a, b))
