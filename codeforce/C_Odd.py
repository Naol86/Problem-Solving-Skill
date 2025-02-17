from collections import Counter


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  count = Counter(nums)
  nums = list(count.keys())
  nums.sort(reverse=True)
  visited = set([])
  i = 0
  while i < len(nums):
    if nums[i] in visited or nums[i] % 2 == 1:
      i += 1
      continue
    visited.add(nums[i])
    if (nums[i]/2) % 2 == 1:
      i += 1
    else:
      nums[i]//=2

  print(len(visited))