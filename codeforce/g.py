import heapq

for _ in range(int(input())):
  n, k = map(int, input().split())
  nums = [int(i) for i in input().split()]
  heap = []
  for i in range(n):
    temp = nums[i] % k
    if temp == 0:
      heapq.heappush(heap, (temp, i))
    else:
      heapq.heappush(heap, ((k - temp), i))
  # print(heap)
  ans = []
  while heap:
    ans.append(heapq.heappop(heap)[1] + 1)
  print(*ans)