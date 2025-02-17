n, k = map(int, input().split())
nums = [int(i) for i in input().split()]
_max = 0
left = 0
right = 0

while right < n:
  if right == 0:
    right += 1
    _max = max(_max, right - left)
    continue
  if nums[right] == nums[right - 1]:
    left = right
    right += 1
    continue
  right += 1
  _max = max(_max, right - left)
  
print(_max)
  