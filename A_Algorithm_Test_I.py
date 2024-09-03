from collections import Counter
import math

x = int(input())
nums = [int(i) for i in input().split()]

count = Counter(nums)
print(math.factorial(len(count)))