for _ in range(int(input())):
  x = int(input())
  s = input()
  ans = []
  t = []
  for i in s:
    if i =='t':
      t.append(i)
    else:
      ans.append(i)
  ans.extend(t)
  print(''.join(ans))