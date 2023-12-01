x = int(input())
lis = []
for i in range(x):
    temp = [int(j) for j in input().split()]
    lis.append(temp)
for i in range(3):
    ans = 0
    for k in range(x):
        ans += lis[k][i]
    if ans != 0:
        print("NO")
        break
else:
    print("YES")