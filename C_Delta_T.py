def check(i):
  return l <= i <= r

for _ in range(int(input())):
  l, r, x = map(int, input().split())
  a, b = map(int, input().split())
  
  if a == b:
    print(0)
    continue
  diff = abs(a - b)
  if diff >= x:
    print(1)
    continue
  if a < b:
    # if check(a + x + diff) == check(a - x) == False:
    #   print(-1)
    #   continue
    if check(a + x + diff):
      print(2)
      continue
    if check(a - x):
      print(2)
      continue

  if a > b:
    if check(a - x - diff) == check(a + x) == False:
      print(-1)
      continue
    if check(a - x - diff):
      print(2)
      continue
    if check(a + x):
      print(2)
      continue
  # print(diff + x  + a, 'diff', _)
  print(3)