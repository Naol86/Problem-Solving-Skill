from collections import defaultdict


for _ in range(int(input())):
  n = int(input())
  nums = [int(i) for i in input().split()]
  nums.sort()
  print(*nums[::-1])