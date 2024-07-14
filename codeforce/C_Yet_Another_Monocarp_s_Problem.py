def check(mid):
  count = 0
  nums.append(nums[-1] + mid)
  for i in range(length):
    if nums[i+1] - nums[i] > mid:
      count += mid
    else:
      count += nums[i+1] - nums[i]
    if count >= k:
      nums.pop()
      return True
  nums.pop()
  return False

for _ in range(int(input())):
  n, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  length = len(nums)
  
  left = 1
  right = k
  
  ans = 0
  
  while left <= right:
    mid = left + (right - left)//2
    if check(mid):
      ans = mid
      right = mid - 1
    else:
      left = mid + 1
  print(ans)