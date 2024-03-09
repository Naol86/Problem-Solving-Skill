import sys

input = sys.stdin.readline

for _ in range(int(input())):
    lis = [int(i) for i in input().split()]
    print(lis[0], lis[1], lis[-1] - lis[0] - lis[1])