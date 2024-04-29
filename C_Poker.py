import heapq
for _ in range(int(input())):
  x = int(input())
  nums = [int(i) for i in input().split()]
  heap = []
  _sum = 0
  size = 0
  i = x - 1
  while i >= 0:
    # if size of heap is less than size
    if nums[i] == 0:
      size += 1
    elif len(heap) < size:
      heapq.heappush(heap, nums[i])
      _sum += nums[i]
    elif heap:
      if heap[0] < nums[i]:
        _sum -= heapq.heapreplace(heap, nums[i])
        _sum += nums[i]
    i -= 1
  print(_sum)
