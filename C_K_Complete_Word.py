from collections import defaultdict


for _ in range(int(input())):
  x, k = map(int, input().split())
  s = input()
  buk = [[] for __ in range(k)]
  for i in range(x):
    buk[i % k].append(s[i])
  # print(buk)
  def find(b):
    count = defaultdict(int)
    _max = 0
    for a in b:
      count[a] += 1
      _max = max(_max, count[a])
    return len(b) - _max
  ans = 0
  left = 0
  right = k - 1
  while left <= right:
    if left == right:
      ans += find(buk[left])
    else:
      ans += find(buk[left] + buk[right])
    left += 1
    right -= 1
  print(ans)