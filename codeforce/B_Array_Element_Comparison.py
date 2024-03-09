import bisect
import sys

input = sys.stdin.readline

x, y = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a.sort()

ans = []

for i in range(y):
    ans.append(bisect.bisect_right(a, b[i]))
print(*ans)