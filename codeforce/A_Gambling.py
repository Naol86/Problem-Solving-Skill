a, b = map(int, input().split())
x = y = z = 0
for i in range(1, 7):
  j = abs(a - i)
  k = abs(b - i)
  if j > k:
    x += 1
  elif k > j:
    y += 1
  else:
    z += 1
print(y, z, x)