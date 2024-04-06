import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    num = int(input())
    x = math.log2(num)
    # print(x)
    if int(x) == x:
        print("NO")
    else:
        print("YES")