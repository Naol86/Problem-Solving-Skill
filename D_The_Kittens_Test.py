z = int(input())

parent = [i for i in range(z)]
size = [1 for i in range(z)]

ans = [[i+1] for i in range(z)]

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
      ans[par_x].extend(ans[par_y])
    else:
      parent[par_x] = par_y
      size[par_y] += size[par_x]
      ans[par_y].extend(ans[par_x])

for _ in range(z - 1):
  x, y = map(int, input().split())
  union(x - 1, y - 1)
a = parent[find(0)]
print(*ans[a])