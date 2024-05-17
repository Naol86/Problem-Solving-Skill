n = int(input())

ls = 0
lr = 0

ar  =[]
for i in range(n):
  a,b = map(int, input().split())
  ar.append((a, b))
  ls += a
  lr += b
  

_max = abs(lr - ls)
col = -1

for i in range(n):
  if abs(ls - ar[i][0] + ar[i][1] - (lr - ar[i][1] + ar[i][0]) )> _max:
    col = i
    _max = abs(ls - ar[i][0] + ar[i][1] - (lr - ar[i][1] + ar[i][0]) )
if col == -1:
  print(0)
else:
  print(col+1)