n, x = map(int, input().split())
c = 0
d = 2 ** 31

for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        if c < a:
            c = a
        if d > b:
            d = b
    else:
        if c < b:
            c = b
        if d > a:
            d = a

if x >= c and x <= d:
    z = 0
else:
    z = abs(x - c) if abs(x - c) < abs(x - d) else abs(x - d)

if c <= d:
    print(z)
else:
    print(-1)
