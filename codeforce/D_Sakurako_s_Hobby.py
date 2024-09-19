parent = []
size = []
def find(x):
  if parent[x] == x:
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


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  s = input()
  parent = [i for i in range(x + 1)]
  size = [1 for i in range(x + 1)]
  ans = []
  for i in range(x):
    if s[i] == '1':
      a = find(i)
      size[a] -= 1
    union(i, nums[i] - 1)
  for i in range(x):
    a = find(nums[i] - 1)
    ans.append(size[a])
  print(*ans)