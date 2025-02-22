n, s = map(int, input().split())

nums = [int(i) for i in input().split()]

def solve(n, s, nums):
  i = 0
  j = 0
  _sum = 0
  _max = 0
  while j < n:
    if _sum + nums[j] < s:
      _sum += nums[j]
      _max = max(_max, j - i + 1)
      j += 1
    else:
      _sum -= nums[i]
      i += 1
  return _max

print(solve(n, s, nums))