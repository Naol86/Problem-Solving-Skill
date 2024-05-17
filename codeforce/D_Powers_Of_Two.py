import heapq


num, b = map(int, input().split())

leng = 0
temp = num
while temp > 0:
  if temp & 1:
    leng += 1
  temp >>= 1
ans = []
if leng > b:
  print("NO")
elif leng == b:
  print("YES")
  i = 0
  while num > 0:
    if num & 1:
      ans.append(1<<i)
    i += 1
    num >>= 1
  print(*ans)
else:
  heap = []
  i = 0
  while num > 0:
    if num & 1:
      heap.append(-(1<<i))
    i += 1
    num >>= 1
  heapq.heapify(heap)
  while len(heap) < b:
    temp = heapq.heappop(heap)
    if temp == -1:
      break
    heapq.heappush(heap, temp//2)
    heapq.heappush(heap, temp//2)
  if len(heap) == b:
    for i in range(len(heap)):
      heap[i] *= -1
    print("YES")
    print(*heap)
  else:
    print("NO")
  