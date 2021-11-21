T = int(input())
if T <= 10:
    for i in range(1, T + 1):
        N = int(input())
        a = []
        if 100000 >= N >= 1:
            for j in range(1, N + 1):
                if N % j == 0:
                    a.append(j)
                else:
                    continue

        print(f"Case {i}: ", end='')
        for k in a:
            print(f"{k}", end=' ')
        print()
