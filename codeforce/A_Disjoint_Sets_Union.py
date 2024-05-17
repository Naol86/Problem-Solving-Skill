n, m = map(int, input().split())

parent = [i for i in range(n)]
size = [1] * n

def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  par_x = find(x)
  par_y = find(y)

  if par_x != par_y:
    if size[par_x] > size[par_y]:
      parent[par_y] = par_x
      size[par_x] += size[par_y]
    else:
      parent[par_x] = par_y
      size[par_y] += size[par_x]

for _ in range(m):
  cmd = input().split()
  if cmd[0] == 'get':
    # print(parent)
    if find(int(cmd[1]) - 1) == find(int(cmd[2]) - 1):
      print("YES")
    else:
      print("NO")
  else:
    union(int(cmd[1]) - 1, int(cmd[2]) - 1)