n, k = map(int, input().split())

nums = [int(i) for i in input().split()]

dp = [0] * (n)

for i in range(1, n):
  _min = float('inf')
  for j in range(1, k + 1):
    if i - j < 0:
      break
    _min = min(_min, abs(nums[i] - nums[i-j]) + dp[i-j])
  dp[i] = _min
print(dp[-1])