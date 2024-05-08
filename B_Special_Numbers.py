for _ in range(int(input())):
  n, k = map(int, input().split())
  ans = 0
  i = 0
  while k > 0:
    if k & 1:
      ans += n ** i
    i += 1
    k >>= 1
  print(ans%(10**9 + 7))