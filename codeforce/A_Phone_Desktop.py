n = int(input())
for _ in range(n):
  x,y = map(int,input().split())
  d = y//2
  r = y%2
  c = (7*d)
  c += (11 * r)
  a = 0
  if x > c:
    x -= c
    a = x//15
    if x%15 != 0:
      a += 1
      
  print(d + r + a)
    