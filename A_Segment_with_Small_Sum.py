x, y = map(int, input().split())
nums = [int(i) for i in input().split()]

left = 0
right = 0
_sum = 0
ans = 0
while right < x:
  _sum += nums[right]
  if _sum > y:
    _sum -= nums[left] + nums[right]
    left += 1
  else:
    ans = max(ans, right - left + 1)
    right += 1

print(ans)