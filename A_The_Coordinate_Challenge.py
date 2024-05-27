for _ in range(int(input())):
  num = int(input())
  ans = {
    0: 0,
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 2
  }
  
  if num == 1:
    print(2)
    continue

  out = num % 6
  final = (num // 6) * 2 + ans[out]
  print(final)
  