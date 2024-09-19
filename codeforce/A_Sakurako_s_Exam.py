for _ in range(int(input())):
  a, b = map(int, input().split())
  if a % 2:
    print("NO")
    continue
  if b % 2 == 0 and a % 2 == 0:
    print("YES")
    continue
  if a >= 2 and a % 2 == 0:
    print("YES")
    continue
  print("NO")