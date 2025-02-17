n, s = map(int, input().split())

nums = [int(i) for i in input().split()]

def solve(n, s, nums):
  i = 0
  j = 0
  _sum = 0
  count = 0
  while j < n:
    if _sum + nums[j] <= s:
      _sum += nums[j]
      j += 1
    else:
      _sum -= nums[i]
      count += (j - i)
      i += 1
  if j > i:
    sn = (j-i)/2 * (1 + (j-i))
    count += sn
  return int(count)

print(solve(n, s, nums))