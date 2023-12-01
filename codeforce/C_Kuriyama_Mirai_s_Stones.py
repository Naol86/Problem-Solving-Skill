x = int(input())
lis = [int(i) for i in input().split()]
lis = [0] + lis
lis_sort = lis.copy()
lis_sort.sort()
for i in range(1,len(lis)):
    lis[i] = lis[i] + lis[i-1]
    lis_sort[i] = lis_sort[i] + lis_sort[i-1]
for i in range(int(input())):
    temp = [int(j) for j in input().split()]
    if temp[0] == 1:
        ans = lis[temp[2]] - lis[temp[1]-1]
        print(ans)
    else:
        ans = lis_sort[temp[2]] - lis_sort[temp[1]-1]
        print(ans)