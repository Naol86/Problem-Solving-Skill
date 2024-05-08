for _ in range(int(input())):
  n,k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  q = [int(i) for i in input().split()]
  # if nums[0] == 1:
  #   print(*[1]*k)
  #   continue
  ans = []
  for i in q:
    if i < nums[0]:
      ans.append(i)
    else:
      ans.append(nums[0] - 1)
  print(*ans)