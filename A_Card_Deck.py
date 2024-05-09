for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  pro = [0]
  for i in range(1, x):
    if nums[i] < nums[pro[-1]]:
      pro.append(pro[-1])
    else:
      pro.append(i)
  # print(pro)
  ans = []
  i = x - 1
  pre = x
  while i >= 0:
    ans.extend(nums[pro[i]:pre])
    pre = pro[i]
    i = pro[i - 1]
    if i == 0:
      ans.extend(nums[pro[i]:pre])
      break
  print(*ans)