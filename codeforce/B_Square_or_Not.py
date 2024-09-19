import math


def solve(y, s):
  l = 0
  r = y
  for i in range(y):
    if i == 0 or i == y - 1:
      for j in range(y):
        if s[l + j] != '1':
          print("No")
          return
    else:
      for j in range(y):
        if j == 0 or j == y - 1:
          if s[l + j] != '1':
            print("No")
            return
        else:
          if s[l + j] != '0':
            print("No")
            return
    l += y
  print("Yes")
  return

for _ in range(int(input())):
  x = int(input())
  s = input()
  y = int(math.sqrt(x))
  if math.sqrt(x) != int(math.sqrt(x)):
    print("No")
    continue
  solve(y, s)