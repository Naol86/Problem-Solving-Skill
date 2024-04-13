from collections import deque
import math


for _ in range(int(input())):
  x = int(input())
  s = [i for i in input()]
  nums = [int(i) for i in input().split()]
  
  visited = set()
  cycle_list = []
  for num in nums:
    if num in visited:
      continue
    node = num
    temp = deque([])
    while node not in visited:
      temp.append(s[node - 1])
      visited.add(node)
      node = nums[node - 1]
    cycle_list.append(temp)
  def count(lis):
    for i in range(1, len(lis)):
      if len(lis) % i != 0:
        continue
      j = 0
      k = i
      while k < len(lis) and lis[j] == lis[k]:
        j += 1
        k += 1
      if k == len(lis):
        return i
    return len(lis)
  
  lcm = 1
  for lis in cycle_list:
    temp = count(lis)
    lcm = math.lcm(lcm, temp)
  print(lcm)