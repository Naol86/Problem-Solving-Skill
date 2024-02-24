temp = []
for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    temp.append((x, lis))


for x, lis in temp:
    pre = 0
    left = 1
    if lis[0] > 0:
        left = 0
        pre = lis[0]
        check = False
    wind = 1
    _max = pre
    for i in range(1, x):
        if -lis[i] > pre:
            pre = 0
            left = i
        else:
            pre += lis[i]
        if _max < pre:
            _max = pre
            wind = max(wind, i - left + 1)
        lis[i] += lis[i - 1]
    if _max >= lis[-1] and wind < x:
        print("NO")
    else:
        print("YES")