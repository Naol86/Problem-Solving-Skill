for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == y:
        print(*[1 for __ in range(x)])
        continue
    if y == 1:
        print(*[i for i in range(1, x + 1)])
    else:
        print(-1)