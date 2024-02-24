import copy


row, col = [int(i) for i in input().split()]
matrix = []
for _ in range(row):
    lis = [int(i) for i in input().split()]
    matrix.append(lis)



temp = copy.deepcopy(matrix)
checked_col = set()
for i in range(row):
    for j in range(col):
        # if j in checked_col:
        #     continue
        if matrix[i][j] == 0:
            for k in range(col):
                temp[i][k] = 0
            for k in range(row):
                temp[k][j] = 0
            checked_col.add(j)


# for i in temp:
#     print(*i)
# print("-------------------------------")
ans = copy.deepcopy(temp)
for i in range(row):
    for j in range(col):
        # if j in checked_col:
        #     continue
        if temp[i][j] == 1:
            for k in range(col):
                ans[i][k] = 1
            for k in range(row):
                ans[k][j] = 1
            checked_col.add(j)


if ans == matrix:
    print("YES")
    for i in temp:
        print(*i)
else:
    print("NO")