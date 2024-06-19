import bisect
import heapq


for _ in range(int(input())):
  n, m, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  models = [int(i) for i in input().split()]
  comp = [int(i) for i in input().split()]
  heap = []
  ans = []
  _max = -1
  a = 0
  b = 0
  for i in range(1, n):
    if _max < nums[i] - nums[i - 1]:
      a = nums[i-1]
      b = nums[i]
      _max = nums[i] - nums[i - 1]
    heapq.heappush(heap, -(nums[i] - nums[i - 1]))
  models.sort()
  comp.sort()
  if m > k:
    upper = comp
    lower = models
  else:
    upper = models
    lower = comp
  ans.append(-heap[0])
  # print(a, b, heap[0])
  def search(left, right, z):
    while left <= right:
      mid = left + (right - left) // 2
      num = lower[mid] + z
      # if num - a < ans[0] and b - num < ans[0]:
      ans[0] = min(ans[0], max(num - a, b - num))
      if num - a > b - num:
        right = mid - 1
      else:
        left = mid + 1
  # print(upper)
  # print(lower)
  for num in upper:
    left_side = bisect.bisect_left(lower, a - num)
    right_side = bisect.bisect_right(lower, b - num)
    # if left_side == right_side:
    #   continue
    search(left_side, right_side - 1, num)
    # print(left_side, right_side, num)
  heapq.heappop(heap)
  heapq.heappush(heap, -ans[0])
  print(-heap[0])