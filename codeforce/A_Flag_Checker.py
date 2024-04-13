
def solve():
  n, m = map(int, input().split())
  lis = []
  for _ in range(n):
    lis.append(input())
  prev = 'x'
  for i in range(n):
    if lis[i][0] == prev:
      print("NO")
      return
    prev = lis[i][0]
    for j in range(m):
      if prev != lis[i][j]:
        print("NO")
        return
  else:
    print("YES")
    return 
solve()