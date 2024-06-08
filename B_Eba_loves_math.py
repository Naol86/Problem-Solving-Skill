for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  ans = nums[0]
  for num in nums:
    ans &= num
  print(ans)