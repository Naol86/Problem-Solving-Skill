import heapq

f, size, q = map(int, input().split())
friends = [int(i) for i in input().split()]

display = set()
heap = []

def add(id):
  heapq.heappush(heap, (friends[id-1], id))
  display.add(id)

for _ in range(q):
  cmd, id = map(int, input().split())
  if cmd == 2:
    if id in display:
      print("YES")
    else:
      print("NO")
  else:
    if len(heap) < size:
      add(id)
    else:
      if heap[0][0] < friends[id - 1]:
        fr, i = heapq.heappop(heap)
        display.remove(i)
        add(id)
