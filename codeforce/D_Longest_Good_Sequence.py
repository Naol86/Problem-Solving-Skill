x = int(input())
nums = [int(i) for i in input().split()]

if x == 1:
  print(1)
else:
  _set = set(nums)

  dp = [0] * (nums[-1]+ 1)
  _max = 0
  for num in range(2, nums[-1] + 1):
    if dp[num]:
      continue
    if num in _set and dp[num] == 0:
      dp[num] = 1
    last = num
    pre = num
    num += num
    while num <= (nums[-1]):
      if num not in _set:
        num += pre
        continue
      dp[num] = max(dp[num], dp[last] + 1)
      _max = max(_max, dp[num])
      last = num
      num += pre
  print(_max)