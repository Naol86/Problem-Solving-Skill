for _ in range(int(input())):
  a, b = map(int, input().split())
  factorial = 1
  for i in range(a, b, -1):
    factorial *= i
  i = 2
  ans = 0
  while factorial > 2:
    while factorial % i == 0:
      ans += 1
      factorial //= i
    i += 1
  print(ans)