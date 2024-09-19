for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  _set = set([nums[0]])
  ans = "YES"
  for num in nums:
    if num not in _set:
      ans = "NO"
      break
    if num - 1 == 0:
      # _set.add(x)
      pass
    else:
      _set.add(num - 1)
    if num + 1 > x:
      # _set.add(1)
      pass
    else:
      _set.add(num + 1)
  print(ans)