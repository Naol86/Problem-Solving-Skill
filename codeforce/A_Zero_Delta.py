for _ in range(int(input())):
  a, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  
  a = 0
  b = len(nums) - 1
  while b < len(nums) and k > 0:
    if nums[a] == 0:
      a += 1
      if b == a:
        b += 1
    else:
      nums[a] -= 1
      nums[b] += 1
      k -= 1
  print(*nums)