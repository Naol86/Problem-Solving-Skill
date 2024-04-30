from collections import defaultdict, Counter

for _ in range(int(input())):
  n, e = map(int, input().split())
  nodes = defaultdict(list)
  for __ in range(e):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)
  pop = []
  leng = []
  for key, val in nodes.items():
    if len(val) == 1:
      pop.append(key)
    else:
      leng.append(len(val))
  for key in pop:
    nodes.pop(key)
  count = Counter(leng)
  # print(count)
  ans = [-1, -1]
  for key, val in count.items():
    if val == 1:
      ans[0] = key
    else:
      ans[1] = key - 1
  if ans[0] == -1:
    ans[0] = ans[1] + 1
  print(*ans)