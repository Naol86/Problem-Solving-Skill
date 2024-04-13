from collections import defaultdict, deque


n = int(input())
graph = defaultdict(list)
count = 0
for _ in range(n-1):
  u,v = [int(i) for i in input().split()]
  graph[u].append(v)
  graph[v].append(u)
init = [int(i) for i in input().split()]
goal = [int(i) for i in input().split()]
count = 0
queue = deque([1,0,False , False , -1])
while queue :
  length = len(queue)
  node,lvl,even,odd,par = queue.popleft()
  if lvl % 2 == 0:
    if even and init[node-1] == goal[node-1]:
      count += 1
  else:
    if odd and init[node-1] == goal[node-1]:
      count += 1
  for neighbor in graph[node]:
    
    pass