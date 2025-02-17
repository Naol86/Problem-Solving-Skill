for _ in range(int(input())):
  a, b, n = map(int, input().split())
  nums = [int(i) for i in input().split()]
  _sum = b
  for num in nums:
    if num > a:
      _sum += (a - 1)
    else:
      _sum += num
  print(_sum )