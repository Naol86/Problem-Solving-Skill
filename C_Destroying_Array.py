from collections import defaultdict


x = int(input())
nums = [int(i) for i in input().split()]
destroy = [int(i) for i in input().split()]

ans = [0]
parent = {}
rep = defaultdict(int) # representation and sum

visited = set()
_max = 0

def find(x):
  if x not in visited:
    return 0
  if x == parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x, y):
  parentX = find(x)
  parentY = find(y)
  if parentX == parentY:
    return rep[parentX]
  parent[parentY] = parentX
  rep[parentX] += rep[parentY]
  return rep[parentX]

for i in range(x-1, 0, -1):
  visited.add(destroy[i])
  temp = nums[destroy[i] - 1]
  rep[destroy[i]] = temp
  parent[destroy[i]] = destroy[i]
  left = find(destroy[i] - 1)
  right = find(destroy[i] + 1)
  # print(destroy[i], left, right)
  if left and right:
    union(left, destroy[i])
    temp = union(left, right)
  if not right and left:
    temp = union(left, destroy[i])
  if not left and right:
    # print('parent ',parent)
    temp = union(right, destroy[i])
    # print("here i am", right, destroy[i], dict(rep))
  _max = max(_max, temp)
  ans.append(_max)
for i in ans[::-1]:
  print(i)
# print(ans)