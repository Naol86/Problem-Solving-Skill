for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  if x == 1:
    print(1)
    print(1)
    continue
  nums = [(nums[i], i + 1) for i in range(x)]
  
  nums.sort()
  # print(nums)
  
  ans = [nums[0][1]]
  _sum = nums[0][0]
  for i in range(1, x):
    if nums[i][0] > _sum:
      ans = [nums[i][1]]
      # ans.append(nums[i][1])
    # elif nums[i][0] == _sum:
    #   ans = [nums[i][1], nums[i-1][1]]
      # ans.append(nums[i][1])
      # ans.append(nums[i-1][1])
    else:
      # ans = []
      ans.append(nums[i][1])
    _sum += nums[i][0]
  print(len(ans))
  ans.sort()
  print(*ans)