from collections import defaultdict


x = int(input())
matrix = []
row = [defaultdict(int) for _ in range(x)]
col = [defaultdict(int) for _ in range(x)]

for i in range(x):
  nums = [int(i) for i in input().split()]
  for j in range(x):
    # print(nums[j],i, end=' ')
    row[i][nums[j]] += 1
    col[j][nums[j]] += 1
  # print()
  matrix.append(nums)

def check(i, j):
  for key, value in row[i].items():
    if value == 0:
      continue
    diff = matrix[i][j] - key
    if diff in col[j] and col[j][diff] != 0:
      return True
  return False


def solve():
  for i in range(x):
    for j in range(x):
      if matrix[i][j] == 1:
        continue
      else:
        row[i][matrix[i][j]] -= 1
        col[j][matrix[i][j]] -= 1
        temp = check(i, j)
        row[i][matrix[i][j]] += 1
        col[j][matrix[i][j]] += 1
        if not temp:
          print("No")
          return
  else:
    print("Yes")
solve()
  
# print(row)
# print(col)
# print(matrix)
