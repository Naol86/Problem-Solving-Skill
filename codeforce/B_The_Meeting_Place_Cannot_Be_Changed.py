import sys

input = sys.stdin.readline

x = int(input())
pos = [int(i) for i in input().split()]
speed = [int(i) for i in input().split()]

left = float('inf')
right = float('-inf')
_min = float('inf')
for i in range(x):
    left = min(left, pos[i])
    _min = min(_min, speed[i])
    right = max(right, pos[i])
    pos[i] = [pos[i], speed[i]]
def took(y):
    time = 0
    for i, j in pos:
        dis = abs(i - y)
        time = max(time, dis/j)
    return time

right = (right - left) / _min * x
left = 0
print(left, right)
ans = right
while left <= right:
    mid = left + (right - left) / 2
    time = took(mid)
    print(time, mid, left)
    ans = min(ans, time)
    if time <= ans:
        right = mid - 0.001
    else:
        left = mid + 0.001
print(ans)