def dfs(vertex, visited):
  # base case
  visited.add(vertex)
  for neighbour in graph[vertex]:
    if neighbour not in visited:
      dfs(neighbour, visited)


# dfs using stack
visited = set()
neighbors = {1:[2,3,4], 2:[1,7], 3:[1,4,5], 4:[1,3], 5:[3,7], 7:[2,5]}
root = 0
state = 0
stack = [(1,state)]
while stack:
  node = stack.pop()
  if node in visited:
    continue
  print(node)
  visited.add(node)
  for neighbor in neighbors[node[0]]:
    if neighbor not in visited:
      stack.append((neighbor, state))