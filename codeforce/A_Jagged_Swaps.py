for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  
  
  for j in range(x**2):
    i = 1
    while i < x - 1:
      if nums[i-1] < nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
      i += 1
  # print(nums)
  for i in range(1, x):
    if nums[i] < nums[i-1]:
      print("NO")
      break
  else:
    print("YES")