import bisect
import sys

input = sys.stdin.readline

x = int(input())

shop = [int(i) for i in input().split()]
shop.sort()

for _ in range(int(input())):
    m = int(input())
    print(bisect.bisect_right(shop, m))
