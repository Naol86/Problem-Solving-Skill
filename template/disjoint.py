# size compression

parent = {}
size = {}

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
# -------------------------------------
# path halving
def find(x):
  while x != parent[x]:
    parent[x] = parent[parent[x]]
    x = parent[x]
  return x