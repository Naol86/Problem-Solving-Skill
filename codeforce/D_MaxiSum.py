x, y = [int(i) for i in input().split()]
lis = [int(i) for i in input().split()]
temp = [0] * (x + 1)
for _ in range(y):
    l, r = [int(i) for i in input().split()]
    temp[l-1] += 1
    temp[r] -= 1

for i in range(1, x + 1):
    temp[i] += temp[i - 1]
temp.pop()
temp.sort(reverse=True)
lis.sort(reverse=True)
ans = 0
for i in range(x):
    ans += (lis[i] * temp[i])
print(ans)