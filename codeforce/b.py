def solve(mat):
  n = len(mat)
  up = [(0, 0)]
  ups = set()
  lows = set()
  low = [(n-1, n-1)]
  ups.add(mat[0][0])
  lows.add(mat[n-1][n-1])
  ans = 1
  
  while True:
    ans *= len(up)  * len(low)
    a, b = [],[]
    _ups = set()
    _lws  =set()
    for x, y in up:
      if x +1 < n:
        a.append((x+1, y))
        _ups.add(mat[x+1][y])
      
      if y+1 < n:
        b.append((x, y+1))
        _ups.add(mat[x][y+1])
    for x, y in low:
      if x - 1 >= 0:
        b.append((x-1, y))
        _lws.add()
  
  
  
  