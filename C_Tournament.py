for _ in range(int(input())):
  n, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  pre= [0]
  for i in range(n-1, -1, -1):
    pre.append(pre[-1] + nums[i])
  pre.reverse()
  count = 0
  div = 1
  for i in range(n):
    if nums[i]//div - k >= nums[i]//(div * 2) or (pre[i + 1]// (n - i) > k and pre[i + 1]// (n - i) - k + nums[i]//div - k > 0):
      count += (nums[i]//div - k)
    else:
      div *= 2
      count += nums[i]//div
    # print(count)
  print(count)