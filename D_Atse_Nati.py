from collections import defaultdict

n, m, k = map(int, input().split())
govern = [int(i) for i in input().split()]
govern_set = set(govern)

parent = {i:i for i in range(1, n + 1)}
size = [1] * (n + 1)
size[0] = 0

def find_max(lis):
  _max = 0
  ind = 1
  for i in range(len(lis)):
    if lis[i] > _max:
      _max = lis[i]
      ind = i
  return ind

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
      size[par_y] = 0
    else:
      parent[par_x] = par_y
      size[par_y] += size[par_x]
      size[par_x] = 0

for _ in range(m):
  a, b = map(int, input().split())
  union(a, b)
max_index = find_max(size)

_set_govern = set()
govern_with_size = []
for i in govern:
  x = find(i)
  _set_govern.add(x)
  govern_with_size.append((size[x], i))
govern_with_size.sort()

for i in range(1, n + 1):
  if size[i] == 0:
    continue
  if find(i) not in _set_govern:
    union(max_index, i)

def cal():
  ans = 0
  for num in size:
    if num:
      ans += (num * (num - 1))//2
  return ans

if find(max_index) in _set_govern:
  ans = cal()
else:
  if k > 0:
    s, g = govern_with_size.pop()
    union(max_index, g)
    ans = cal()
  else:
    ans = cal()
if ans - m >= 0:
  print(ans - m)
else:
  print(0)
