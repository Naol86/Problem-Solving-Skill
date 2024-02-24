for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    _max = max(x, y)
    _min = min(x, y)
    temp = _max * 2
    while True:
        if temp % _min == 0:
            if temp / (_max * _min) <= _min and temp / (_max * _min) > 0 or temp // (_min * _max) == _max:
                break
        temp += _max
    print(temp)