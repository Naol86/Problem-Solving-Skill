n, k = map(int, input().split())
nums = [int(i) for i in input().split()]

ans = 1
_sum = sum(nums[:k])
_min = _sum
left = 0
right = k
while right < n:
  _sum += (nums[right] - nums[left])
  if _sum < _min:
    ans = left + 2
    _min = _sum
  right += 1
  left += 1
print(ans)