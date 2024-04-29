parent = {}
child = {}



for _ in range(int(input())):
  old, new = input().split()
  if old not in child:
    parent[old] = new
    child[new] = old
  else:
    child[new] = child[old]
    parent[child[old]] = new
    child.pop(old)
  # print(parent)
  # print(child)
  # print('-------------------')

print(len(parent))
for key, val in parent.items():
  print(key, val)
