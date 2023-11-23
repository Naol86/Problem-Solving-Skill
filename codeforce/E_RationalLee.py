for k in range(int(input())):
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    z = [int(i) for i in input().split()]
    y.sort()
    ans = 0
    for i in z:
        _max1 = max(y[-i:])
        _min1 = min(y[-i:])
        y.pop()
        ans += _max1 + _min1
    print(ans)