T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        S = str(input()).lower()
        if len(S) <= 1000:
            a = S[::-1]
            if S == a:
                print("Yes! it is palindrome!")
            else:
                print("Sorry! It is not palindrome!")
