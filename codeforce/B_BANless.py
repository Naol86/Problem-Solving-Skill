import math


for _ in range(int(input())):
  x = int(input())
  last = 3 * x
  first = 1
  ans = math.ceil(x/2)
  print(ans)
  for i in range(ans):
    print(first, last)
    first += 3
    last -= 3