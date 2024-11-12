import math


for _ in range(int(input())):
  x = int(input())
  x = math.gcd(100, x)
  # print(math.gcd(100, x), 'asdf')
  if (100/x == 100//x):
    print(100//x)
  elif (100/(100-x) == 100//(100-x)):
    print(100//(100-x))
  else:
    print(100)