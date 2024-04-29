x = int(input())

nums = [int(i) for i in input().split()]

parent = [i for i in range(x)]
size = [1] * x
ans = [x]
def find(x):
  # print(x)
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  par_x = find(x)
  par_y = find(y)
  if par_x != par_y:
    ans[0] -= 1
    if size[par_x] > size[par_y]:
      parent[par_y] = par_x
      size[par_x] += size[par_y]
    else:
      parent[par_x] = par_y
      size[par_y] += size[par_x]

for i in range(x):
  # print('i is ', i)
  union(i, nums[i]-1)
print(ans[0])