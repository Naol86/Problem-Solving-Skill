import bisect


x, y = [int(i) for i in input().split()]

nums = [0] + [int(i) for i in input().split()]

for i in range(1, x + 1):
    nums[i] += nums[i - 1]

ans = 0
pos =  1
while pos < x + 1:
    insert = bisect.bisect_right(nums, nums[pos - 1] + y)
    ans = max(ans, insert - pos)
    if insert == x + 1:
        break
    pos += 1
print(ans)