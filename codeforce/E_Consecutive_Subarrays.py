n, k = map(int, input().split())

nums = [int(i) for i in input().split()]

for i in range(len(nums) - 2, -1,-1):
  nums[i] += nums[i + 1]
ans = nums[0]
k -= 1
nums = nums[1:]
nums.sort(reverse=True)
i = 0
while k > 0:
  ans += nums[i]
  i += 1
  k -= 1
print(ans)