x = int(input())
nums = [int(i) for i in input().split()]

index = 0
_min = float('inf')
for i in range(x-2):
  temp = nums[i + 2] - nums[i]
  if _min > temp:
    index = i + 1
    _min = temp
nums[index] = nums[index - 1]
_max = 0
for i in range(1, x):
  _max = max(_max, nums[i] - nums[i-1])
print(_max)