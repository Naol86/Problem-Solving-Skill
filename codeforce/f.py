l, p, k =map(int, input().split())
for _ in range(l):
  x = input()
  ans = []
  for ch in x:
    for _ in range(k):
      ans.append(ch)
  ans = ''.join(ans)
  for _ in range(k):
    print(ans)