for _ in range(int(input())):
  x = int(input())
  lis = []

  _max = 9

  while _max < x:
    lis.append(str(_max))
    x -= _max
    _max -= 1

  lis.append(str(x))
  num = int("".join(lis[::-1]))

  print(num)