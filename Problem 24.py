T = int(input())
if 1 <= T <= 100:
    for i in range(T):
        array_element_number = int(input())
        n = []
        for m in range(array_element_number):
            b = int(input())
            n.append(b)
        print(n[::2])
