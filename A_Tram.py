_max = 0
_sum = 0
for _ in range(int(input())):
  a, b = map(int, input().split())
  _sum += b - a
  _max = max(_max, _sum)
print(_max)