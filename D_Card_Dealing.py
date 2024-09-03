for _ in range(int(input())):
  n = int(input()) - 1
  a = 1
  b = 0
  turn = False
  step = 2
  while n > (step * 2) + 1:
    num = step * 2 + 1
    if turn:
      a += num
    else:
      b += num
    n -= num
    step += 2
    turn = not turn

  if turn:
    a += n
  else:
    b += n
  print(a, b)