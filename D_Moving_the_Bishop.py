x = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())

mat = []
for _ in range(x):
  mat.append([i for i in input()])

if (ax + ay) % 2 != (bx + by) % 2:
  print(-1)
else:
  pass
# print(mat)