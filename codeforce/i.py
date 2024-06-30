from sys import stdin

input = stdin.readline


for _ in range(int(input())):
  n,k = map(int, input().split())
  
  ps = [0] * 55
  
  for _ in range(n):
    l, r = map(int, input().split())
    if k >= l and k <= r:
      ps[l-1] += 1
      ps[r] -= 1
      
  for i in range(1, len(ps)):
    ps[i] += ps[i-1]
  
  m = max(ps)
  if ps[k-1] == m and ps.count(m) == 1:
    print("YES")
  else:
    print("NO")