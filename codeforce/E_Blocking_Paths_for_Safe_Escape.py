from collections import deque


t = int(input())
for _ in range(t) :
    m , n = [int(i) for i in input().split()]
    maze = []
    good = 0
    for __ in range(m) :
        l = [i for i in input()]
        good += l.count('G')
        maze.append(l)
    dir = [(1 , 0) , (0 , -1) , (-1 , 0), (0 , 1)]
    def block_bad(row, col):
        if row == m - 1 and col == n - 1:
            return False
        temp = True
        for r, c in dir:
            new_r = row + r
            new_c = col + c
            if new_r >= m or new_r < 0 or new_c >= n or new_c < 0:
                temp = temp and True
            elif maze[new_r][new_c] == 'G':
                return False
            elif maze[new_r][new_c] == '.':
                maze[new_r][new_c] = '#'
        return temp
    def get_bad():
        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'B':
                    temp = block_bad(i, j)
                    if not temp:
                        return False
        if maze[m -1][n - 1] == '#' or maze[m -1][n - 1] == 'B':
            return False
        return True
    def bfs(good):
        queue = deque([(m-1, n-1)])
        while queue:
            row, col = queue.popleft()
            for r, c in dir:
                if row + r >= m or row + r < 0 or col + c >= n or col + c < 0:
                    continue
                if maze[row + r][col + c] == 'G':
                    good -= 1
                    queue.append((row + r, col + c))
                    maze[row + r][col + c] = '#'
                elif maze[row + r][col + c] == '.':
                    maze[row + r][col + c] = '#'
                    queue.append((row + r, col + c))
        return good


    if not get_bad():
        if good == 0 and maze[m -1][n-1] != 'B':
            print("Yes")
        else:
            print("No")
    else:
        good = bfs(good)
        if good == 0:
            print("Yes")
        else:
            print("No")