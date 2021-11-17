T = int(input())

if 1 <= T <= 100:
    for i in range(T):
        n = (input())
        if n.isupper():
            print("Uppercase Character")
        elif n.islower():
            print("Lowercase Character")
        elif n.isdigit():
            print("Numeric Digit")
        else:
            print("Special Character")