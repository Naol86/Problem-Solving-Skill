import math


for _ in range(int(input())):
  _max = 0
  ans = 0
  x = int(input())
  for i in range(1, x):
    gcd = math.gcd(x, i)
    if gcd + i > _max:
      ans = i
      _max = gcd + i
  print(ans)