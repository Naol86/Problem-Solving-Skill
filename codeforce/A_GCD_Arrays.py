from math import ceil
for _ in range(int(input())):
  a,b, c = map(int, input().split())
  if a == b and a > 1:
    print("YES")
  else:
    diff = b - a
    if a%2 ==0:
      d = diff // 2
    else:
      d = ceil(diff/2)
    if b%2 == 1:
      d += 1
    if c >= d:
      print("YES")
    else:
      print("NO")