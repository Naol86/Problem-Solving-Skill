for _ in range(int(input())):
  x = int(input())
  count = 0
  while x > 1:
    count += 1
    if x % 2 == 0:
      x //= 2
      continue
    elif x % 3 == 0:
      x = (2 * x)//3
      continue
    elif x % 5 == 0:
      x = (4 * x) // 5
      continue
    break
  if x == 1:
    print(count)
  else:
    print(-1)