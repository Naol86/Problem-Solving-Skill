for _ in range(int(input())):
  a, b = map(int, input().split())
  nums = [int(i) for i in input().split()]
  _max = max(nums)
  for __ in range(b):
    x = input().split()
    if x[0] == '+':
      if int(x[2]) >= _max >= int(x[1]):
        _max += 1
    else:
      if int(x[2]) >= _max >= int(x[1]):
        _max -= 1
    print(_max, end=' ')
  print()