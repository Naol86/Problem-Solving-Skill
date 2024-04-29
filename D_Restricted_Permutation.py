import heapq
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
inDegree = [0] * n
for _ in range(m):
  a, b = map(int, input().split())
  graph[a-1].append(b)
  inDegree[b-1] += 1
# print(graph)
# print(inDegree)
heap = []
for i in range(n):
  if inDegree[i] == 0:
    heapq.heappush(heap, i)
ans = []
while heap:
  x = heapq.heappop(heap)
  ans.append(x + 1)
  for node in graph[x]:
    inDegree[node - 1] -= 1
    if inDegree[node - 1] == 0:
      heapq.heappush(heap, node - 1)
if len(ans) == n:
  print(*ans)
else:
  print(-1)
