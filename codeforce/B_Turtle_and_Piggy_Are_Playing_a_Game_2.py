for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  nums.sort()
  right = x - 1
  left = 0
  l = True
  while right - left != 0:
    if l:
      left += 1
    else:
      right -= 1
    l = not l
  print(nums[left])