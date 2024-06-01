from collections import deque


def bfs(graph, node):
  visited = set([node])
  queue = deque([node])
  _list = []
  while queue:
    node = queue.popleft()
    _list.append(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  return _list