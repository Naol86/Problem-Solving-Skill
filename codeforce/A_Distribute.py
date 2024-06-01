x = int(input())

nums = [int(i) for i in input().split()]

for i in range(x):
  nums[i] = [nums[i], i + 1]
nums.sort()

i = 0
while i < x //2:
  print(nums[i][1], nums[-i-1][1])
  i += 1