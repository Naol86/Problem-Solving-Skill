from collections import deque


for _ in range(int(input())):
  s = input()
  ans = deque()
  for a in s:
    ans.append(a)
    ans.appendleft(a)
  print(''.join(ans))