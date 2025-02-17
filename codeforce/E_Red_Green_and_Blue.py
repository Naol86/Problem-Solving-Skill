import heapq


def cal(x, y, z):
  return (x-y)**2 + (y-z)**2 + (z-x)**2

for _ in range(int(input())):
  a, b, c = map(int, input().split())
  nums_a = [int(i) for i in input().split()]
  nums_b = [int(i) for i in input().split()]
  nums_c = [int(i) for i in input().split()]
  nums_a.sort(reverse=True)
  nums_b.sort(reverse=True)
  nums_c.sort(reverse=True)
  x, y, z = nums_a.pop(), nums_b.pop(), nums_c.pop()
  _min = cal(x, y, z)
  
  while nums_a or nums_b or nums_c:
    if nums_a:
      a = cal(nums_a[-1], y, z)
    else:
      a = float('inf')
    if nums_b:
      b = cal(x, nums_b[-1], z)
    else:
      b = float('inf')
    if nums_c:
      c = cal(x, y, nums_c[-1])
    else:
      c = float('inf')
    
    if a <= b and a <= c:
      _min = min(_min, a)
      x = nums_a.pop()
    elif b <= a and b <= c:
      _min = min(_min, b)
      y = nums_b.pop()
    else:
      _min = min(_min, c)
      z = nums_c.pop()
  print(_min)