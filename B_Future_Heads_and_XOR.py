a, b = map(int, input().split())

def base3(nums):
  lis = []
  while nums:
    lis.append(nums%3)
    nums//=3
  return lis

a = base3(a)
b = base3(b)

if len(a) != len(b):
  diff = abs(len(a) - len(b))
  if len(a) < len(b):
    a.extend([0] * diff)
  else:
    b.extend([0] * diff)
# a.reverse()
# b.reverse()

# print(a)
# print(b)

def solve(x, y):
  _sum = 0
  for i in range(len(x)):
    if x[i] == y[i]:
      _sum += (0)
    elif y[i] > x[i]:
      _sum += ((y[i] - x[i]) * (3 ** i))
    elif y[i] == 0:
      _sum += ((3 - x[i]) * (3 ** i))
    else:
      n = 3 + y[i] - x[i]
      # print(n, i)
      _sum += (n * (3 ** i))
  return _sum


# print(solve(a, b), solve(b, a))    

print(solve(a,b))