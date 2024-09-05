for _ in range(int(input())):
  x = int(input())
  ans = x // 4
  remi = x % 4
  if remi == 0:
    print(ans)
  else:
    print(ans + 1)