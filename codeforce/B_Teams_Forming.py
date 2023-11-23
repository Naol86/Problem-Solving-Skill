x = int(input())
lis = [int(i) for i in input().split()][:x]
lis.sort()
ans = 0
for i in range(x//2):
    ans += lis[int(2*i) + 1] - lis[int(2*i)]
print(ans)