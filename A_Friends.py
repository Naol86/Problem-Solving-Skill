a = int(input())
b = int(input())

c = abs(a - b)
if c % 2:
  c -= 1
  c //= 2
  last = c + 1
  _sum = c/2 * (1 + c) 
  _sum *= 2
  # print(last, _sum)
  print(int(_sum + last))
else:
  c //= 2
  _sum = c/2 * (1 + c) 
  _sum *= 2
  # print(c)
  print(int(_sum))