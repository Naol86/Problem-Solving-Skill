from collections import deque

def solve():
  board_size = int(input())
  ax, ay = map(int, input().split())
  bx, by = map(int, input().split())
  ax-=1
  ay-=1
  bx-=1
  by-=1

  mat = []
  for _ in range(board_size):
    mat.append([i for i in input()])

  queue = deque()
  pos = [(-1,-1), (-1,1), (1,-1), (1,1)]
  def go(x, y, dir):
    i, j = pos[dir]
    while True:
      x += i
      y += j
      if x < 0 or y < 0 or x >= board_size or y >= board_size:
        break
      if mat[x][y] == '#':
        break
      if (x,y) == (bx, by):
        return True
      mat[x][y] = '#'
      queue.append((x,y))
    return False

  if (ax + ay) % 2 != (bx + by) % 2:
    print(-1)
    return 
  if (ax, ay) == (bx, by):
    print(0)
    return 
  else:
    level = 0
    queue.append((ax, ay))
    mat[ax][ay] = '#'
    while queue:
      length = len(queue)
      for _ in range(length):
        x, y = queue.popleft()
        for i in range(4):
          temp = go(x, y, i)
          if temp:
            print(level + 1)
            return 
      level += 1
    pass

  print(-1)
  return
solve()
# print(mat)