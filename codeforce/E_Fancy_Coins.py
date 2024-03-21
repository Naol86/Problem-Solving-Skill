for _ in range(int(input())):
    m, k, a, ak = [int(i) for i in input().split()]
    x = m // k
    y = m % k
    # print(x, y)
    if ak > 0:
        if ak <= x:
            x -= ak
            ak = 0
        else:
            ak -= x
            x = 0
    if ak > 0 and y > k:
        temp = y // k
        if ak <= temp:
            y -= (ak * k)
            ak = 0
        else:
            ak -= temp
            y -= (temp * k)
    if a > 0:
        if y >= a:
            y -= a
            a = 0
        else:
            a -= y
            y = 0
    if (x * k) - k >= 0 and a >= k:
        temp = a // k
        if temp >= x:
            a -= (x * k)
            x = 0
        else:
            x -= temp
    count = x + y
    print(count)