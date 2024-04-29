from collections import deque


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  not_leave = set(nums)
  colors = input()
  outDegree = [0] * x
  graph = [[colors[i] == 'W', colors[i] == 'B'] for i in range(x)] # white, black
  queue = deque()
  for i in range(1, x + 1):
    if i not in not_leave:
      queue.append(i)
    if i < x:
      outDegree[nums[i-1] - 1] += 1


  while queue:
    node = queue.popleft()
    outDegree[nums[node - 2] - 1] -= 1
    graph[nums[node - 2] - 1][0] += graph[node - 1][0]
    graph[nums[node - 2] - 1][1] += graph[node - 1][1]
    if outDegree[nums[node - 2] - 1] == 0 and nums[node - 2] != 1:
      queue.append(nums[node - 2])
  # print(graph)
  count = 0
  for a, b in graph:
    count += a == b
  print(count)