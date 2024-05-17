from collections import Counter


x = int(input())
nums = [0] + [int(i) for i in input().split()]

counter = Counter(nums)
_max = 0
ans = 0
for key , val in counter.items():
  if (key * val) > _max:
    _max = key * val
    ans = key
visited = set([ans])
for i in range(1, x-1):
  if nums[i] in visited:
    continue
  if nums[i] != ans and nums[i + 1] != ans and nums[i-1] != ans:
    _max += nums[i]
    visited.add(nums[i+1])
    visited.add(nums[i-1])
print(_max)