for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    _sum = 0
    for __ in range(x):
        w, l = [int(i) for i in input().split()]
        _sum += max(w, l)
    if _sum >= y:
        print("YES")
    else:
        print("NO")