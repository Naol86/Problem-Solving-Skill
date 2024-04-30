import heapq

x = int(input())
heap = []


ans = []
for _ in range(x):
  cmd = [i for i in input().split()]
  if len(cmd) == 1:
    if not heap:
      ans.append('insert 0')
      # heapq.heappush(heap, 0)
    else:
      heapq.heappop(heap)
    ans.append(' '.join(cmd))
  elif len(cmd) == 2 and cmd[0] == 'insert':
    heapq.heappush(heap, int(cmd[1]))
    ans.append(' '.join(cmd))
  else:
    while len(heap) and heap[0] < int(cmd[1]):
      heapq.heappop(heap)
      ans.append('removeMin')
    if heap and heap[0] == int(cmd[1]):
      pass
    else:
      heapq.heappush(heap, int(cmd[1]))
      ans.append(f'insert {cmd[1]}')
    ans.append(' '.join(cmd))
print(len(ans))
for i in ans:
  print(i)