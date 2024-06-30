for _ in range(int(input())):
  n, k, x = map(int, input().split())
  ans = []
  for i in range(k, 0, -1):
    if i == x:
      continue
    mod = n % i
    if mod <= k and mod != x:
      ans.extend([i] * (n // i))
      if mod != 0:
        ans.append(n % i)
      print("YES")
      print(len(ans))
      print(*ans)
      break
  else:
    print("NO")