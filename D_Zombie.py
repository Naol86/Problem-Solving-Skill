from collections import defaultdict


n, k = map(int, input().split())
graph = defaultdict(list)
visited = set()
for _ in range(k):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# print(graph)
ans = [0]

def dfs(node):
  if len(graph[node]) == 1 and node != 1:
    return 0
  visited.add(node)
  nums = [0]
  for n in graph[node]:
    if n not in visited:
      nums.append(dfs(n) + 1)
  # print(nums)
  nums.sort()
  if len(nums) == 1:
    ans[0] = max(ans[0], nums[0])
  else:
    ans[0] = max(ans[0], nums[-1] + nums[-2])
  return nums[-1]

dfs(1)
print(ans[0])