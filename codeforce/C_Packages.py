for _ in range(int(input())):
  n, k = map(int, input().split())
  if n <= k:
    print(1)
  else:
    ans = n
    i = 2
    while i * i < n and i <= k:
      if n % i == 0:
        print(i)
        break
      i += 1
    else:
      print(ans)