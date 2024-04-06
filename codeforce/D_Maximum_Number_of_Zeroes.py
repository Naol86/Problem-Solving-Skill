from collections import defaultdict
import math


x = int(input())
lis1 = [int(i) for i in input().split()]
lis2 = [int(i) for i in input().split()]

count = defaultdict(int)

dont = 0
for i in range(x):
    if lis1[i] == 0:
        if lis2[i] == 0:
            dont += 1
        continue
    if lis2[i] == 0:
        count[(0,0)] += 1
    # gcd = (lis2[i])/(lis1[i])
    gcd = math.gcd(abs(lis2[i]), abs(lis1[i]))
    temp = (lis1[i] * lis2[i])
    if temp > 0:
        temp = 1
    else:
        temp = -1
    # print(a)
    
    count[(temp * (abs(lis2[i])//gcd), (abs(lis1[i])//gcd))] += 1
    # count[()] += 1
# print(count)
_max = 0

for key, value in count.items():
    _max = max(_max, value)
print(_max + dont)