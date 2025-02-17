import math
for _ in range(int(input())):
  n, k = map(int, input().split())
  health = [int(i) for i in input().split()]
  position = [int(i) for i in input().split()]
  nums = [[abs(position[i]), health[i]] for i in range(n)]
  nums.sort()
  time = 0
  i = 0
  rem = 0
  while i < n:
    nums[i][1] -= rem
    time += math.ceil(nums[i][1]/k)
    if time > nums[i][0]:
      print("NO")
      break
    if nums[i][1] % k != 0:
      rem = k - nums[i][1] % k
    else:
      rem = 0
    i += 1
  else:
    print("YES")