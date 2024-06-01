class solution:
  def find(self,x):
    if x == self.dic[x]:
      return x
    self.dic[x] = self.find(self.dic[x])
    return self.dic[x]
  def union(self,x,y):
    xp = self.find(x)
    yp = self.find(y)
    if xp == yp:
      return
    if self.size[xp] < self.size[yp]:
      xp,yp = yp,xp
    self.dic[yp] = xp
    self.size[xp] += self.size[yp]
  def solve(self,n,m):
    self.dic = {x:x for x in range(1,n+1)}
    self.size = {x:1 for x in range(1,n+1)}
    for _ in range(m):
      x,y = map(int,input().split())
      self.union(x,y)
    for key in self.dic:
      self.find(key)
    xp = self.dic[1]
    yp = self.dic[n]
    if xp == yp:
      print("YES")
    else:
      print("NO")
obj = solution()
t = int(input())
for _ in range(t):
  n,m = map(int,input().split())
  obj.solve(n,m)
