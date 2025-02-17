import heapq


n, s = map(int, input().split())
nums = [int(i) for i in input().split()]

def check(mid):
  _sum = 0
  heap = []
  i = 0
  while i < n:
    temp = (nums[i] + (i + 1) * mid)
    if len(heap) == mid:
      if heap and -heap[0] > temp:
        x = heapq.heappop(heap)
        _sum += x
        _sum += temp
        heapq.heappush(heap, -temp)
      else:
        i += 1
        continue
    elif _sum + temp > s:
      if heap and -heap[0] > temp:
        x = heapq.heappop(heap)
        _sum += x
        _sum += temp
        heapq.heappush(heap, -temp)
      else:
        i += 1
        continue
    else:
      _sum += temp
      heapq.heappush(heap, -temp)
    i += 1
  return (len(heap), _sum)

left = 0
right = n
ans = 0
val = 0

while left <= right:
  mid = left + (right - left)//2
  amount, cost = check(mid)
  # print(amount, mid, 'adafdsf')
  if amount != mid:
    right = mid - 1
  elif cost <= s:
    if amount > ans:
      ans = amount
      val = cost
    left = mid + 1
  else:
    right = mid - 1
print(ans, val)