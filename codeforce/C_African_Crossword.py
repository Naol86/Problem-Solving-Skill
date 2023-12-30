from collections import Counter
x, y = [int(i) for i in input().split()]
matrix = []
row_set = []
for _ in range(x):
    row = input()
    matrix.append([i for i in row])
    count = Counter(row)
    temp = set()
    for key, value in count.items():
        if value == 1:
            temp.add(key)
    row_set.append(temp)

matrix = matrix
col_set = []
for i in range(y):
    lis = []
    for k in range(x):
        lis.append(matrix[k][i])
    temp = set()
    count = Counter(lis)
    for key, value in count.items():
        if value == 1:
            temp.add(key)
    col_set.append(temp)
ans = []
for i in range(x):
    for j in range(y):
        if matrix[i][j] in row_set[i] and matrix[i][j] in col_set[j]:
            ans.append(matrix[i][j])
print("".join(ans))