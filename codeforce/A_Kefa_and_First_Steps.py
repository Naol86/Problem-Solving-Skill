x = int(input())
nums = [int(i) for i in input().split()]

_max = 0
i = 0
j = 1
while j < x:
  if nums[j-1] > nums[j]:
    _max = max(_max, j - i)
    i = j
  j += 1
_max = max(_max, j - i)
print(_max)