for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    a = max(lis[0], lis[1])
    b = min(lis[0], lis[1])
    for i in range(2, x):
        if lis[i] > a:
            b = a
            a = lis[i]
        elif lis[i] > b:
            b = lis[i]

    ans = []
    for i in range(x):
        if lis[i] == a:
            ans.append(lis[i] - b)
        else:
            ans.append(lis[i] - a)
    print(*ans)