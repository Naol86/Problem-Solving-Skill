import heapq


for _ in range(int(input())):
  p1, p2, p3 = map(int, input().split())
  if (p1 + p2) % 2 != p3 % 2:
    print(-1)
  else:
    if (p1 + p2) <= p3:
      print(p1+p2)
    else:
      print(int(((p1 + p2) - p3) // 2) + p3)