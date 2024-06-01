for _ in range(int(input())):
  def solve():
    matrix = []
    for __ in range(int(input())):
      matrix.append(input())
    for i in range(len(matrix) - 1):
      for j in range(len(matrix) - 1):
        if matrix[i][j] == '1':
          if matrix[i+1][j] == '0' and matrix[i][j+1] == '0':
            return 'NO'
    return "YES"
  print(solve())