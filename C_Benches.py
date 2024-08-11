
n = int(input())
m = int(input())
k = m
nums = []
for _ in range(m):
  x = int(input())
  nums.append(x)
nums.sort()
need = 0

for num in nums:
  need = nums[-1] - num

if need > m:
  print(nums[-1], nums[-1] + k)
else:
  m -= need
  if m % n:
    print(nums[-1] + (k/), nums[-1] + k)