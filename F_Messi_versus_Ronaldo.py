for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  bits = [0] * 60
  for num in nums:
    i = 0
    while num > 0:
      if num & 1:
        bits[i] += 1
      i += 1
      num >>= 1
  _sum = 0
  for num in nums:
    i = 0
    _and = 0
    _or = 0
    while i < 60:
      # and
      if num & 1 and bits[i] > 0:
        _and += (1<<i) * bits[i]

      # or
      if num & 1 or bits[i] > 0:
        # temp = (1<<i)
        # if num & 1:
        #   temp *= x
        # _or += temp
        
        # if bit is set 
        if num & 1:
          _or += (1 << i) * x
        else:
          _or += (1 << i) * bits[i]
      i += 1
      num >>= 1
    _sum += (_and * _or)
  print(_sum % (10 ** 9 + 7))