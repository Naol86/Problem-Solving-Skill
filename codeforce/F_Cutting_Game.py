def solve():
  n,m, c, op = map(int, input().split())
  
  mt = []
  ps = [[0 for _ in range(m+1)] for _ in range(n+1)]
  
  for _ in range(c):
    x, y = map(int, input().split())
    ps[x][y] += 1
    
  for i in range(1, 1+n):
    for j in range(1, m+1):
      ps[i][j] += ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1]
  
  u, d, l, r = 0,n+1,0,m+1
  
  for _ in range(op):
    dr, nm = input().split()
    nm = int(nm)
    if dr == "L":
      y = ps[d][nm] - ps[d][l] - ps[u][nm] + ps[u][l]
      l = max(l, nm - 1)
    elif dr == "R":
      y = ps[d][r-1] - ps[u-1][r-1] - ps[d][l] + ps[]