n, s = map(int, input().split())
nums = [int(i) for i in input().split()]


def solve(n, s, nums):
  _min = float('inf')
  i = 0
  j = 0
  _sum = 0
  while j < n:
    if _sum + nums[j] < s:
      _sum += nums[j]
      j += 1
    else:
      _min = min(_min, j - i + 1)
      _sum -= nums[i]
      i += 1
  if _min == float('inf'):
    return -1
  return _min

print(solve(n, s, nums))