import bisect


for _ in range(int(input())):
  _min = 0
  _max = float("inf")
  n = int(input())
  removed = []
  for __ in range(n):
    a, b = map(int, input().split())
    if a == 1:
      _min = max(_min, b)
    elif a == 2:
      _max = min(_max, b)
    else:
      removed.append(b)
  # print(_min, _max)
  if _min >= _max:
    print(0)
    continue
  temp = _max - _min + 1
  removed.sort()
  x = bisect.bisect_left(removed, _min)
  y = bisect.bisect_right(removed, _max)
  # print(removed, y - x, _min, _max)
  temp -= (y - x)
  print(temp)