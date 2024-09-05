def check(a, b, c):
  return c - a + b - c

for _ in range(int(input())):
  a, b = map(int, input().split())
  c = b
  ans = float('inf')
  for i in range(a, b + 1):
    ans = min(ans, check(a, b, i))
  print(ans)
