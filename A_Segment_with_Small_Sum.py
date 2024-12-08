n, s = map(int, input().split())
nums = [int(i) for i in input().split()]


left = 0
right = 0
_sum = 0

_max = 0

"""
  s = 10
  nums = [13, 4, 1, 5]
  right = 4
  left = 1
  _sum = 10
  _max = 3
"""


while right < n:
  _sum += nums[right]
  # if to check if the sum is valid 
  if _sum <= s:
    _max = max(_max, right - left + 1)
    right += 1
  else:
    _sum -= nums[left]
    _sum -= nums[right]
    if left == right:
      _sum = 0
      right += 1
    left += 1

print(_max)
  