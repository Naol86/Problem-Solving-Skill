from collections import defaultdict


for _ in range(int(input())):
  input()
  n, k = map(int, input().split())
  friends = [int(i) for i in input().split()]
  nodes = defaultdict(list)
  