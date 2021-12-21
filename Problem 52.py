
string = input()
sub = input()

count = start = 0
while True:
    start = string.find(sub, start) + 1
    if start > 0:
        count+=1
    else:
        continue
print(count)
