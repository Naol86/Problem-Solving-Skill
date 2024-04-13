from collections import deque

queue = deque()

queue.append('naol')
queue.append('samuel')

print(queue.popleft())
queue.append('abdu')

print(queue[0])

print(queue.popleft())

