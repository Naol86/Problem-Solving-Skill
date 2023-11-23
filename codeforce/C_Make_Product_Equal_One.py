x = int(input())
lis = [int(i) for i in input().split()][:x]
ans = 0
temp = True
zero = 0
for i in lis:
    if i == 0:
        zero += 1
    elif i < 0:
        ans += -(i + 1)
        temp = not temp
    else:
        ans += (i -1)
if temp or zero != 0:
    print(ans+zero)
else:
        print(ans+2)