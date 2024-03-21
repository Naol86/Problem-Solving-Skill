x, y = [int(i) for i in input().split()]

pos = {(1,1):1, (-1,1):2, (-1,-1):3, (1,-1):4}

if x == 0 and y == 0:
    print(0)
    exit()
elif x == 1 and y == 0:
    print(0)
    exit()

if x == 0:
    x = -(abs(y) // y)
if y == 0:
    y = 1 if x > 0 else -1

dis = (abs(x) - 1) * 4
dis = (abs(y) - 1) * 4 if abs(y) > abs(x) else dis

x = abs(x) // x
y = abs(y) // y

pos = pos[(x, y)]

print(pos + dis)