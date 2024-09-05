import math


for _ in range(int(input())):
  x, y, k = map(int, input().split())
  x_step = math.ceil(x / k)
  y_step = math.ceil(y / k)
  if x_step > y_step:
    print(x_step * 2 - 1)
  else:
    print(y_step * 2)