for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    _max = _sum = lis[0]
    left = 0
    right = left + 1
    while right < x:
        while left < right and lis[right - 1] % 2 == lis[right] % 2:
            _sum -= lis[left]
            left += 1
            _max = max(_max, _sum)
        _sum += lis[right]
        _max = max(_max, _sum)
        right += 1
    print(_max)