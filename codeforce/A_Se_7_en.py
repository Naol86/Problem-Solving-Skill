for _ in range(int(input())):
  x = int(input())
  if x % 7 == 0:
    print(x)
  else:
    rem = x % 7
    ten = x - (x%10)
    ten += 10
    if x - rem + 7 < ten:
      print(x - rem + 7)
    else:
      print(x - rem)