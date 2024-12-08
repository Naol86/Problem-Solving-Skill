for _ in range(int(input())):
  a, b, k = map(int, input().split())
  diff = a - b
  if k % 2 == 0:
    print(diff * (k // 2))
  else:
    print(diff * (k // 2) + a)