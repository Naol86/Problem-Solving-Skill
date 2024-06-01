from collections import defaultdict, deque


n, m = map(int, input().split())
nodes = defaultdict(list)
in_degree = defaultdict(int)

for _ in range(m):
  a, b = input().split()
  nodes[a].append(b)
  in_degree[b] += 1
queue = deque()
for key in nodes:
  if in_degree[key] == 0:
    queue.append(key)
ans = []
while queue:
  course = queue.popleft()
  ans.append(course)
  for node in nodes[course]:
    in_degree[node] -= 1
    if in_degree[node] == 0:
      queue.append(node)
if len(ans) != n:
  print("IMPOSSIBLE")
else:
  print(*ans)