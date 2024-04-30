import heapq


for _ in range(int(input())):
  x = int(input())
  nums = [-int(i) for i in input().split()]
  for i in range(x):
    nums[i] = [nums[i], i+1]
  heapq.heapify(nums)
  ans = []
  count = 0
  while nums:
    a = heapq.heappop(nums)
    if nums and a[0] != 0:
      b = heapq.heappop(nums)
      if b[0] == 0:
        heapq.heappush(nums, a)
        continue
      ans.append((a[1], b[1]))
      count += 1
      a[0] += 1
      b[0] += 1
      if a[0] < 0:
        heapq.heappush(nums, a)
      if b[0] < 0:
        heapq.heappush(nums, b)
  print(count)
  for i in ans:
    print(*i)