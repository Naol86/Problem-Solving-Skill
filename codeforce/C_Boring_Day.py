for _ in range(int(input())):
  n, l, r = map(int, input().split())
  nums = [int(i) for i in input().split()]
  
  left = 0
  right = 0
  win = 0
  _sum = 0
  for i in range(n):
    _sum += nums[i]
    while _sum > r:
      _sum -= nums[left]
      left += 1
    if _sum >= l and _sum <= r:
      win += 1
      left = i + 1
      _sum = 0
  print(win)
