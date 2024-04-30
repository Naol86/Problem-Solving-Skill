for _ in range(int(input())):
  n, k = map(int, input().split())
  ans = []
  i = 0
  while n > 0:
    ans.append(chr(ord('a') + i % k))
    n -= 1
    i += 1
  print(''.join(ans))