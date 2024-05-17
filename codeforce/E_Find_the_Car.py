for _ in range(int(input())):
  n, k, m = map(int, input().split())

  points = [0] + [int(i) for i in input().split()]
  time = [0] + [int(i) for i in input().split()]

  speed = []

  for i in range(1, k+1):
    x = (points[i] - points[i-1])/(time[i] - time[i-1])
    speed.append(x)
  for _ in range(m):
    dis = int(input())
    i = 1
    ans = 0
    
    while dis > 0 :
      if dis < (points[i] - points[i-1]):
        ans += (dis / speed[i - 1])
        dis -= dis
      else:
        ans += ((points[i] - points[i-1]) / speed[i-1])
        dis -= (points[i] + points[i-1])
      # print(dis, ans)
      i += 1
    print(int(ans), end=' ')
  print()