for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  pre = [0]
  for num in nums:
    pre.append(pre[-1] + num)
  # print(pre)
  s = input()
  left = 0
  right = x - 1
  ans = 0
  while left < right:
    if s[left] == 'L' and s[right] == 'R':
      ans += (pre[right + 1] - pre[left])
      left += 1
      right -= 1
    elif s[left] == 'R':
      left += 1
    elif s[right] == 'L':
      right -= 1
    elif nums[left] < nums[right]:
      left += 1
    else:
      right -= 1
  print(ans)