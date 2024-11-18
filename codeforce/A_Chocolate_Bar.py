for _ in range(int(input())):
  n, l, r, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  nums.sort()
  # print(nums)
  count = i = 0
  while i < n and k - nums[i] >= 0:
    if l <= nums[i] <= r:
      count += 1
      k -= nums[i]
    i += 1
  print(count)