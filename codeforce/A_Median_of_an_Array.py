import bisect
import math


for _ in range(int(input())):
    x = int(input())
    nums = [int(i) for i in input().split()]
    nums.sort()
    mid = math.ceil(x / 2) - 1
    x = bisect.bisect_right(nums[mid + 1:], nums[mid])
    print(x + 1)
    