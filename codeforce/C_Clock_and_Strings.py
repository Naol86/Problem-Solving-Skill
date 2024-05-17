for _ in range(int(input())):
  a,b,c,d = map(int, input().split())
  x = min(a, b)
  y = max(a, b)
  diff = 12 - y
  x = (x + diff) % 12
  y = (y + diff) % 12
  c = (c + diff) % 12
  d = (d + diff) % 12
  if (c >= x) and (d >= x):
    print("NO")
  elif (c <= x) and (d <= x):
    print("NO")
  else:
    print("YES")