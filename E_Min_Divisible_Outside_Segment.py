for _ in range(int(input())):
  l, r, d = map(int, input().split())
  # left = float('inf')
  # right = float('inf')
  if l > d or r < d:
    print(d)
  else:
    right = r - (r % d) + d
    print(right)