from collections import defaultdict, deque

n = int(input())

red = set()
black = set([1])

nodes = defaultdict(set)
for _ in range(n - 1):
  a, b = map(int, input().split())
  nodes[a].add(b)
  nodes[b].add(a)

queue = deque([(1, True)])
while queue:
  pop = queue.popleft()
  for i in nodes[pop[0]]:
    if i in red or i in black:
      continue
    if pop[1]:
      red.add(i)
      queue.append((i, False))
    else:
      black.add(i)
      queue.append((i, True))

print(len(black) * len(red) - (n - 1))

# ans = 0
# for y in range(1, n+1):
#   key = y
#   val = nodes[y]
#   if key in red:
#     diff = black.difference(val)
#     ans += len(diff)
#     for i in diff:
#       # nodes[key].add(i)
#       nodes[i].add(key)
#   else:
#     diff = red.difference(val)
#     ans += len(diff)
#     for i in diff:
#       # nodes[key].add(i)
#       nodes[i].add(key)
#   # print(diff)
# print(ans)
