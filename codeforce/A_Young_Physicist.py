a = int(input())
x = y = z = 0
for _ in range(a):
  m = list(map(int, input().split()))
  x += m[0]
  y += m[1]
  z += m[2]
if x == y == z and x == 0:
  print("YES")
else:
  print("NO")