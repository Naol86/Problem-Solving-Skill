from collections import Counter


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  count = Counter(nums)
  ans = float('inf')
  index = -1
  for i in range(x):
    if count[nums[i]] == 1 and nums[i] < ans:
      ans = nums[i]
      index = i + 1
  print(index)