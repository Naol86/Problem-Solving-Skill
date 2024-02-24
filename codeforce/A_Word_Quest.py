for _ in range(int(input())):
    lis = []
    check = True
    ans = []
    for i in range(8):
        x = input()
        lis.append(x)
        if check:
            for j in range(8):
                if x[j] != '.':
                    row = i
                    col = j
                    check = False
    # print(lis,row,col)
    for i in range(row,8):
        if lis[i][col] != '.':
            ans.append(lis[i][col])
        else:
            break
    print("".join(ans))