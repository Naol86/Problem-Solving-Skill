from collections import defaultdict, deque


x = int(input())

pos = [int(i) for i in input().split()]
final = [-1] * x

mat = defaultdict(list)
for i in range(1, x + 1):
  left = i - pos[i - 1]
  right = i + pos[i - 1]
  if left > 0:
    mat[i].append(left)
  if right <= x:
    mat[i].append(right)
print(mat)
# queue = node, dis, even/odd, parent
visited = set()
for i in range(1, x + 1):
  if i in visited:
    continue
  stack = [(i, i % 2, 0)]
  cur = 0
  while stack:
    g = 0
    lis = mat[stack[-1][0]]
    while g < len(lis) and stack:
      # print(stack)
      if lis[g] != stack[-1][1]:
        node, p, dis = stack.pop()
        visited.add(node)
        final[node - 1] = cur - dis
      else:
        cur += 1
        stack.append((lis[g], lis[g] % 2, cur))
        g += 1
print(*final)