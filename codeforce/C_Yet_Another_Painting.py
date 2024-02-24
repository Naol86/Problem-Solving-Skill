for _ in range(int(input())):
    red = int(input())
    lis_red = [0] + [int(i) for i in input().split()]
    blue = int(input())
    lis_blue = [0] + [int(i) for i in input().split()]
    prefix_red = lis_red.copy()
    prefix_blue = lis_blue.copy()
    _max_r = 0
    _max_b = 0
    for i in range(1, red + 1):
        prefix_red[i] = prefix_red[i] + prefix_red[i-1]
        _max_r = max(_max_r, prefix_red[i])
    # print(prefix_red, lis_red)
    for i in range(1, blue + 1):
        prefix_blue[i] = prefix_blue[i] + prefix_blue[i-1]
        _max_b = max(_max_b, prefix_blue[i])
    # print(prefix_blue, lis_blue)
    print(_max_b + _max_r)