x, y = map(int, input().split())

parent = [i for i in range(x)]
min_max = [[i+1,i+1] for i in range(x)]
size = [1 for i in range(x)]

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
      min_max[par_x] = [min(min_max[par_x][0], min_max[par_y][0]), max(min_max[par_x][1], min_max[par_y][1])]
      parent[par_y] = par_x
      size[par_x] += size[par_y]
    else:
      min_max[par_y] = [min(min_max[par_x][0], min_max[par_y][0]), max(min_max[par_x][1], min_max[par_y][1])]
      parent[par_x] = par_y
      size[par_y] += size[par_x]
for _ in range(y):
  cmd = input().split()
  if cmd[0] == 'union':
    union(int(cmd[1]) - 1, int(cmd[2]) - 1)
  else:
    x = find(int(cmd[1]) - 1)
    print(*min_max[x], size[x])
