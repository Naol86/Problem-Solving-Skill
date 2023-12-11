lis = []
row = -1
col = -1
check = True
for i in range(5):
    lis = [int(i) for i in input().split()]
    if check:
        for j in range(5):
            if lis[j] == 1:
                row = i
                col = j
                check = False
ans = abs(2-row)+abs(2-col)
print(ans)