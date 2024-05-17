import math


for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  # nums.append(nums[-1] + 1)
  ans = [nums[0] + 1]
  for i in range(x-1):
    start = nums[i]
    if start < ans[-1]:
      temp = math.floor(ans[-1]/start) + 1
      # print(temp, start)
      temp = temp * start
      temp += ans[-1] % start
      ans.append(temp)
    else:
      ans.append(start)
  print(*ans)