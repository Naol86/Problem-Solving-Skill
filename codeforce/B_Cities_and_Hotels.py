n, d = map(int, input().split())

nums = [int(i) for i in input().split()]
nums.sort()
_set = set([])

for i in range(n):
  if i == 0:
    _set.add(nums[i] - d)
  if i == n - 1:
    _set.add(nums[i] + d)
  if i < n - 1:
    if nums[i] + (d * 2) <= nums[i+1]:
      _set.add(nums[i] + d)
  if i > 0:
    if nums[i] - (d * 2) >= nums[i-1]:
      _set.add(nums[i] - d)
print(len(_set))
