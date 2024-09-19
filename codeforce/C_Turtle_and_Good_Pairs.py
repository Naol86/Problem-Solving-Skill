for _ in range(int(input())):
  x = int(input())
  s = [i for i in input()]
  left = []
  right = []
  s.sort()
  l = True
  for i in s:
    if l:
      left.append(i)
    else:
      right.append(i)
    l = not l
  left.extend(right[::-1])
  print(''.join(left))