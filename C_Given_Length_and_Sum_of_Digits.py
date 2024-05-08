a, b = map(int, input().split())

ans = []
c = b / a
if (b == 0 and a > 1) or c > 9:
  print(-1, -1)
else:
  num = b
  large = []
  while len(large) < a:
    if num >= 9:
      large.append('9')
      num -= 9
    elif num < 9:
      large.append(str(num))
      num -= num
    else:
      large.append('0')
  ans.append(''.join(large))
  if large[-1] != '0' or len(large) == 1:
    ans.append(''.join(large[::-1]))
  else:
    for i in range(len(large) - 1, -1, -1):
      if large[i] != '0':
        large[i] = str(int(large[i]) - 1)
        break
    large[-1] = '1'
    ans.append(''.join(large[::-1]))
  print(*ans[::-1])