from collections import defaultdict, deque

n, m = map(int, input().split())

nodes = defaultdict(list)
for _ in range(m):
  a, b = map(int, input().split())
  nodes[a].append(b)
  nodes[b].append(a)

visited = set()

def extend_to_set(key):
  visited.add(key)
  for i in nodes[key]:
    visited.add(i)

count = 0
for key, val in nodes.items():
  if key not in visited:
    if len(val) > 2:
      extend_to_set(key)
      continue
    queue = deque([key])
    temp = set()
    parent = key
    while queue:
      node = queue.popleft()
      if len(nodes[node]) > 2 or node in visited:
        extend_to_set(node)
        break
      if node in temp:
        count += 1
        break
      temp.add(node)
      if nodes[node][0] != parent:
        queue.append(nodes[node][0])
      elif len(nodes[node]) > 1:
        queue.append(nodes[node][1])
      parent = node

    for i in temp:
      visited.add(i)

print(count)
