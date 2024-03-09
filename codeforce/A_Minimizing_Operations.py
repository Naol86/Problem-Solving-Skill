for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    _min = float('inf')
    _max = -float('inf')
    for i in lis:
        _min = min(_min, i)
        _max = max(_max, i)
    print(_max - _min)