from collections import defaultdict


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  dic = defaultdict(int)
  ans = 0
  for num in nums:
    ans += dic[num.bit_length()]
    dic[num.bit_length()] += 1
  print(ans)