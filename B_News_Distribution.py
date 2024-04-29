x, y = map(int, input().split())
parent = [i for i in range(x)]
size = [1 for _ in range(x)]

def find(x):
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  par_x = find(x)
  par_y = find(y)
  
  if par_x == par_y:
    return True
  if size[par_x] > size[par_y]:
    parent[par_y] = par_x
    size[par_x] += size[par_y]
  else:
    parent[par_x] = par_y
    size[par_y] += size[par_x]

for _ in range(y):
  nums = [int(i) for i in input().split()]
  for i in range(1, nums[0]):
    union(nums[i]-1, nums[i + 1]-1)
ans = []
for i in range(x):
  par = find(i)
  ans.append(size[par])
print(*ans)