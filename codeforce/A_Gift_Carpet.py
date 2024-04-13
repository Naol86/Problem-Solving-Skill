for _ in range(int(input())):
  n, m = map(int, input().split())
  lis = []
  for __ in range(n):
    lis.append([i for i in input()])
  if m < 4:
    print("NO")
    continue
  ans = ['v', 'i', 'k', 'a']
  pos = 0
  for ___ in range(m):
    for i in range(n):
      if lis[i][___] == ans[pos]:
        pos += 1
        break
    if pos == 4:
      break
  if pos == 4:
    print("YES")
  else:
    print("NO")