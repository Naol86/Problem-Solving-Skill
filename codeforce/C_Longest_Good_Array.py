for _ in range(int(input())):
  a, b = map(int, input().split())
  count = 1
  i = 1
  while a + i <= b:
    a += i
    count += 1
    i += 1
  print(count)
  