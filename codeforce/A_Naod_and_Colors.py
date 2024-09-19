from collections import Counter


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  count = Counter(nums)
  ans = 1
  for key, value in count.items():
    ans = max(value, ans)
  print(ans)