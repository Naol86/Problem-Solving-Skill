from sys import stdin

input = stdin.readline

def wat(h, nms):
  wt = 0
  for i in range(len(nms)):
    wt += max(h- nms[i], 0)
  return wt

for _ in range(int(input())):
  n, x = map(int, input().split())
  
  nums = [int(i) for i in input().split()]
  
  l = 0
  r = 10**9 + max(nums) + 10
  while l <= r:
    mid = (l + r) // 2
    y = wat(mid, nums)
    if  y <= x:
      res = mid
      l = mid + 1
    else:
      r = mid - 1
  print(res)