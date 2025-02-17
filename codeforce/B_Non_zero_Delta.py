n, a, b = map(int, input().split())

b %= n
ans = (a + b)%n

if ans == 0:
  print(n)
else:
  print(ans)
# print((a + b)%n)