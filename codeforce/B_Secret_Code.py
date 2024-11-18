from collections import deque


n = int(input())
s = input()

ans = deque([s[0]])
left = True if n % 2 else False
i = 1
while i < n:
  if left:
    ans.appendleft(s[i])
  else:
    ans.append(s[i])
  i += 1
  left = not left
print(''.join(ans))
