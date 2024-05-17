for _ in range(int(input())):
  n, m = map(int, input().split())
  x = input()
  y = input()
  ans = 0
  i = j = 0
  while i < n and j < m:
    if x[i] == y[j]:
      ans += 1
      i += 1
    j += 1
  print(ans)