for _ in range(int(input())):
  n, x, m = map(int, input().split())
  left = x
  right = x
  for __ in range(m):
    l, r = map(int, input().split())
    if l > right or r < left:
      continue
    left = min(left, l)
    right = max(right, r)
  print(right - left + 1)