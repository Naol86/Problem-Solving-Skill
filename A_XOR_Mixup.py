for _ in range(int(input())):
  y = int(input())
  nums = [int(i) for i in input().split()]
  x = nums[0]
  for i in range(1, y):
    x ^= nums[i]
  for i in range(y):
    x ^= nums[i]
    if x == nums[i]:
      print(nums[i])
      break
    x ^= nums[i]
