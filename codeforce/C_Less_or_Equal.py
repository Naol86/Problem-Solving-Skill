from collections import Counter


x, y = [int(i) for i in input().split()]
lis = [int(i) for i in input().split()]
lis.sort()
lis.append(lis[-1] + 1)
count = Counter(lis)
if y == 0:
    if lis[0] == 1:
        print(-1)
    else:
        print(1)
elif x == y or lis[y-1] != lis[y]:
    print(lis[y-1])
else:
    print(-1)