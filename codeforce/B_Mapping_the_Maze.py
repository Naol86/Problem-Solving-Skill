from collections import defaultdict, Counter


n,m = map(int,input().split())

nodes = defaultdict(int)

for _ in range(m):
  a, b = map(int,input().split())
  nodes[a] += 1
  nodes[b] += 1

edges = nodes.values()
count = Counter(edges)

if len(count) == 1 and count[2] == n:
  print("ring topology")
elif len(count) == 2:
  if count[1] == 2 and count[2] == n - 2:
    print("bus topology")
  elif count[1] == n - 1 and count[n-1] == 1:
    print("star topology")
  else:
    print("unknown topology")
else:
  print("unknown topology")

