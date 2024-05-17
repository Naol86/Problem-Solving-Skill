n = int(input())

ans = []
temp = 0
if n == 0:
  print(1)
  print(1)
else:
  while n & (n+1) != 0:
    i = n.bit_length() - 1
    while n & (1<<i):
      i -= 1
    ans.append(i + 1)
    n ^= (1<<(i+1))-1
    if n & (n+1) == 0:
      temp = -1
      break
    n += 1
  if not ans:
    print(0)
  else:
    print(len(ans) * 2 + temp)
    print(*ans)
