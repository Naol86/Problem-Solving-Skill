x = int(input())
nums = [float('inf')] + [int(i) for i in input().split()]

dp = [0] * (x + 1)
dp[0] = float('inf')

for i in range(2, x + 1):
  dp[i] = min(abs(nums[i] - nums[i-1]) + dp[i-1], abs(nums[i] - nums[i-2]) + dp[i-2])
print(dp[-1])