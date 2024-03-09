import sys

input = sys.stdin.readline

points = [int(i) for i in input().split()]
points.sort()

dis = points[1] - points[0] + points[2] - points[1]
print(dis)