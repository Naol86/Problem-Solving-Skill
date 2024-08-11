x, y = map(int, input().split())
nums = [int(i) for i in input().split()]

if y == 1:
  print(min(nums))
elif y == 2:
  print(max(nums[0], nums[-1]))
else:
  print(max(nums))