from collections import Counter


for _ in range(int(input())):
  x = input()
  count = Counter(x)
  nums = list(count.values())
  _max = max(nums)
  if _max == 4:
    print(-1)
  elif _max == 3:
    print(6)
  elif _max <= 2:
    print(4)
  # print(nums)