for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    s = input()
    _min = y
    whit = 0
    for i in range(y):
        if s[i] == 'W':
            whit += 1
    _min = min(_min, whit)
    left = 0
    right = y
    while right < x:
        if s[left] == 'W':
            whit -= 1
        if s[right] == 'W':
            whit += 1
        _min = min(_min, whit)
        right += 1
        left += 1
    print(_min)