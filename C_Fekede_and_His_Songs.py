
import bisect


n, m = map(int, input().split())
nums = []
time = 0
for i in range(n):
  a, b = map(int, input().split())
  time += (a * b)
  nums.append(time)
  
# print(nums)
lis = [int(i) for i in input().split()]
for num in lis:
  x = bisect.bisect_left(nums, num)
  print(x + 1)