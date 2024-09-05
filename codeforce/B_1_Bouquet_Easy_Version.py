from collections import Counter

def calculate(m, c, k):
  x = m // c
  if x > k:
    return k
  return x

for _ in range(int(input())):
  n, m = map(int, input().split())
  nums = [int(i) for i in input().split()]
  # count = Counter(nums)
  # keys = list(count.keys())
  ans = 0
  nums.sort()
  if nums[0] > m:
    print(0)
    continue
  left = 0
  right = 0
  _sum = 0
  while right < n:
    while (nums[right] - nums[left] > 1 or _sum + nums[right] > m) and left < right:
      _sum -= nums[left]
      left += 1
    if _sum + nums[right] <= m:
      _sum += nums[right]
    else:
      left += 1
      right += 1
    right += 1
    # print(_sum)
    ans = max(ans, _sum)
  print(ans)