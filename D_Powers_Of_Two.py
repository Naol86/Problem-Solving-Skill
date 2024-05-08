import heapq


n, k = map(int, input().split())

if k > n:
  print("NO")
elif k == n:
  print(*([1] * k))
elif k == 1:
  if n & (n - 1) == 0:
    print("YES")
    print(n)
  else:
    print("NO")
else:
  lis = []
  i = 0
  while n > 0:
    if n & 1:
      lis.append(-(2**i))
    i += 1
    n >>= 1
  if len(lis) > k:
    print("NO")
  elif len(lis) == k:
    print("YES")
    lis = [-i for i in lis]
    print(*lis)
  else:
    heapq.heapify(lis)
    while len(lis) != k:
      x = heapq.heappop(lis)
      if x == -1:
        print("NO")
        break
      heapq.heappush(lis, (x//2))
      heapq.heappush(lis, (x//2))
    else:
      for i in range(len(lis)):
        lis[i] *= -1
      print("YES")
      print(*lis)
  pass