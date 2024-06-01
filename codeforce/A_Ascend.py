x = int(input())
nums = [int(i) for i in input().split()]

left = 0
right = 1
_max = 1
while right < x:
  if nums[right - 1] >= nums[right]:
    left = right
  _max = max(_max, right - left + 1)
  right += 1
print(_max)