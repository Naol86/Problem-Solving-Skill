from collections import Counter


for _ in range(int(input())):
  n = int(input())
  nums = [int(i) for i in input().split()]
  count = Counter(nums)
  keys = list(count.keys())
  keys.sort()
  if keys[0] != 0:
    print(0)
    continue
  if keys[0] == 0 and count[0] == 1:
    print(0)
    continue
  i = 0
  cost = 0
  while n > 0:
    # print(count[i], 'asdf')
    if i not in count:
      count[i-1] -= 1
      cost += i
      if count[i-1] == 1:
        i -= 1
      n -= 1
    elif count[i] == 1:
      cost += i
      count.pop(i)
      i-= 1
      n -= 1
    else:
      i += 1
    i = max(i, 0)
  print(cost)