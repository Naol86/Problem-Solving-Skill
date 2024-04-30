from collections import defaultdict


x = int(input())


mat = defaultdict(list)

nodes = [int(i) for i in input().split()]

for i in range(x - 1):
  mat[nodes[i]].append(i + 2)
# print(mat)

colors = [int(i) for i in input().split()]

stack = [(1,0)]
count = 0
while stack:
  node, color = stack.pop()
  if colors[node - 1] == color:
    for n in mat[node]:
      if n != node:
        stack.append((n, color))
  else:
    count += 1
    for n in mat[node]:
      if n != node:
        stack.append((n, colors[node - 1]))
print(count)