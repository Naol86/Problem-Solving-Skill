for _ in range(int(input())):
  n = int(input())
  if n == 2:
    print(-1)
    continue
  matrix = [[0 for i in range(n)] for j in range(n)]
  num = 1
  print(*matrix)
  
  for i in range(n):
    x = 0
    y = i
    for j in range(n-i):
      matrix[x][y] = num
      num += 1
      x += 1
      y += 1
  print(*matrix)
  for i in range(1, n):
    x = i
    y = 0
    for j in range(n-i):
      matrix[x][y] = num
      num += 1
      x += 1
      y += 1
  print(*matrix)