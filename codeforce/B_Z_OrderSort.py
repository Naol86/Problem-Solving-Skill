x = int(input())
lis = [int(i) for i in input().split()]
lis.sort()
left = 0
right = x - 1
ans = []
while left < right:
    ans.append(lis[left])
    ans.append(lis[right])
    left += 1
    right -= 1
if left == right:
    ans.append(lis[left])
print(*ans)