for _ in range(int(input())):
  a, b, k = map(int, input().split())
  lis_a = [i for i in input()]
  lis_b = [i for i in input()]
  lis_a.sort(reverse=True)
  lis_b.sort(reverse=True)
  c = []
  
  count = 0
  pre = -1
  
  while lis_a and lis_b:
    if count != k:
      if lis_a[-1] < lis_b[-1]:
        c.append(lis_a.pop())
        if pre != 0:
          pre = 0
          count = 0
        count += 1
      else:
        c.append(lis_b.pop())
        if pre != 1:
          pre = 1
          count = 0
        count += 1
    else:
      if pre != 0:
        c.append(lis_a.pop())
        pre = 0
      else:
        c.append(lis_b.pop())
        pre = 1
      count = 1
  print(''.join(c))