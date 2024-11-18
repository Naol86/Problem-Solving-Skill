for _ in range(int(input())):
  num = int(input())
  div = num // 4
  rem = num % 4
  if rem == 0:
    print(num//4)
  else:
    if rem == 1 and div > 1:
      print(div - 1)
    elif rem == 2 and div > 0:
      print(div)
    elif rem == 3 and div > 2:
      print(div - 1)
    else:
      print(-1)