for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  
  count = 0
  i = 0
  while i < x - 1:
    if nums[i] % 2 == nums[i + 1] % 2:
      count += 1
      nums[i + 1] *= nums[i]
    i += 1
  
  print(count)