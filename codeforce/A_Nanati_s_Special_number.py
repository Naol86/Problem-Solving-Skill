for _ in range(int(input())):
    x = int(input())
    s = input()
    _max = 'a'
    for i in range(x):
        _max = max(_max, s[i])
    print(ord(_max) - ord('a') + 1)