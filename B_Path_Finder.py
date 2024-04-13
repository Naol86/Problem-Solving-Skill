from collections import defaultdict, deque


x = int(input())
mat = defaultdict(list)
for _ in range(x - 1):
  u, v, c = map(int, input().split())
  mat[u].append((v, c))
  mat[v].append((u, c))

visited = set()
queue = deque([(0,0)])
_max = 0
while queue:
  leng = len(queue)
  for _ in range(leng):
    node, dis = queue.popleft()
    for n, d in mat[node]:
      if n in visited:
        continue
      queue.append((n, dis + d))
      _max = max(_max, d + dis)
    visited.add(node)
print(_max)