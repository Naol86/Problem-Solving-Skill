for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  if nums[0] != len(nums):
    print("NO")
    continue
  height = len(nums)
  stack = []
  temp = 0
  i = len(nums) - 1
  while i >= 0:
    while stack and i >= 0 and temp == nums[i]:
      i -= 1
    if i < 0:
      break
    stack.append((i + 1, nums[i] - temp))
    temp = nums[i]
    i -= 1
  ans = []
  for i, j in stack:
    ans += [i] * j
  if ans == nums:
    print("YES")
  else:
    print("NO")
  # print(ans)
  # print("YES")