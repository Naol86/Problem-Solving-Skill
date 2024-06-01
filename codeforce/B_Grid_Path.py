for _ in range(int(input())):
  n, m, k = map(int, input().split())

  matrix = [[float('inf')] * (m + 1) for __ in range(n + 1)]
  matrix[1][1] = 0
  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if i == 1 and j == 1:
        continue
      matrix[i][j] = min(j + matrix[i-1][j], i + matrix[i][j-1])
  if matrix[-1][-1] == k:
    print("YES")
  else:
    print("NO")