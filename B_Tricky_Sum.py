

for _ in range(int(input())):
  n = int(input())
  
  # print(math.log2(n), x)
  _sum = int(n/2) * (n + 1)
  
  x = 1
  while x <= n:
    _sum -= (2 * x)
    x *= 2
  
  # print(count)
  print(_sum)