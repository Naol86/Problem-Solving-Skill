import sys

input = sys.stdin.readline

x, y = map(int, input().split())

while y > 0:
    last = x % 10
    if last == 0:
        x //= 10
        y -= 1
    else:
        if last <= y:
            x -= last
            y -= last
        else:
            x -= y
            y = 0
print(x)