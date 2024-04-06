import math


for _ in range(int(input())):
  x, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  
  nums[0] -= k
  gcd = nums[0]
  _min = nums[0]
  _max = nums[0]
  for i in range(1, x):
    nums[i] -= k
    gcd = math.gcd(gcd, nums[i])
    _min = min(_min, nums[i])
    _max = max(_max, nums[i])
  # print(gcd,'gcd')
  if _min == _max:
    print(0)
    continue
  if _min <= 0 and _max >= 0:
    print(-1)
    continue
  ans = 0
  for num in nums:
    ans += abs(num//gcd) - 1
  print(ans)