a, b = map(int, input().split())

x = max(a, b)
y = min(a, b)

if x == y:
  print(0)
else:
  dis = x - y
  dis = dis.bit_length()
  i = 0
  while dis > 0:
    x |= 1<<i
    i += 1
    dis -= 1
  print(x)