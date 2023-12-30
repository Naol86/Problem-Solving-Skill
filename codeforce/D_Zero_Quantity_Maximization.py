from collections import defaultdict
import math
loops = int(input())
nums_1 = [int(i) for i in input().split()]
nums_2 = [int(i) for i in input().split()]
count = defaultdict(int)
_max = 0
zero = 0

for i in range(loops):
    if nums_1[i] != 0:
        gcd = math.gcd(abs(nums_1[i]),abs(nums_2[i]))
        x, y = abs(nums_2[i])//gcd , abs(nums_1[i])//gcd
        x = x * -1 if nums_1[i] * nums_2[i] < 0 else x
    elif nums_2[i] == 0:
        zero += 1
        continue
    else:
        continue
    count[(x,y)] += 1
    _max = max(_max, count[(x,y)])
print(_max + zero)
