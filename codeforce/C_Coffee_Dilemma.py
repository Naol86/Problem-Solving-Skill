import heapq

heap = []
cup = 0

x = int(input())
nums = [int(i) for i in input().split()]

_sum = 0
for num in nums:
  if num >= 0:
    _sum += num
    cup += 1
  elif _sum + num >= 0:
    heapq.heappush(heap, num)
    _sum += num
    cup += 1
  else:
    if heap and heap[0] < num:
      _sum -= heapq.heapreplace(heap, num)
      _sum += num
# print(heap)
print(cup)