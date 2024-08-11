for _ in range(int(input())):
  a, b, c, n = map(int, input().split())
  _max = max(a, b, c)
  
  need = (_max - a) + (_max - b) + (_max - c)
  
  if need > n:
    print("NO")
  else:
    n -= need
    if n % 3 == 0:
      print("YES")
    else:
      print("NO")