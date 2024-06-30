for _ in range(int(input())):
  n = int(input())
  mat = []
  for __ in range(n):
    mat.append([ord(i) - ord('a') for i in input()])
  dir = [[(-1,0), (0,1)], [(0,1), (1,0)], [(1,0),(0,-1)], [(0,-1), (-1,0)]]
  limit = [0,0]
  right = [0,0]
  left = [n-1, 0]
  operation = 1
  ans = 0
  temp = 0
  while operation <= n//2:
    while left != limit:
      # print(left, right)
      if mat[right[0]][right[1]] != mat[left[0]][left[1]]:
        if mat[right[0]][right[1]] < mat[left[0]][left[1]]:
          ans += (abs(mat[left[0]][left[1]] - mat[right[0]][right[1]]))
          mat[right[0]][right[1]] = mat[left[0]][left[1]]
        else:
          ans += (temp * abs(mat[left[0]][left[1]] - mat[right[0]][right[1]]))
      right[0] += dir[temp][1][0]
      right[1] += dir[temp][1][1]
      left[0] += dir[temp][0][0]
      left[1] += dir[temp][0][1]
    temp += 1
    # print(left, right)
    # print(dir[temp])
    limit = right.copy()
    # print(limit)
    # print(right)
    # break
    if temp == 4:
      # print('-----------------')
      limit[0] += 1
      limit[1] += 1
      right = limit.copy()
      left[0] -= 1
      left[1] += 1
      temp = 0
      operation += 1
      # print(limit, dir[temp])
      # break
  print(ans)