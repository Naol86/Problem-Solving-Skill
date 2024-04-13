for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  ans = [nums[0]]
  i = 1
  for i in range(1, x):
    while ans[-1] > nums[i]:
      ans.append(nums[i])
    ans.append(nums[i])
  print(len(ans))
  print(*ans)