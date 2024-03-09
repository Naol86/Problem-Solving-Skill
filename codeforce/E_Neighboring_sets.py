from collections import defaultdict
from math import factorial
def comb(a,b):
    if a - b < 0:
        return 0
    one = factorial(a)
    two = factorial(a - b)
    three = factorial(b)
    return one / (two * three)

temp = []
for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    lis.sort()
    temp.append((lis,x))

for lis, x in temp:
    index = defaultdict(int)
    for i in range(x):
        index[lis[i]] = i
    count = 0
    for i in range(x):
        for j in range(3):
            # print(lis[i],"here",lis[i] + 2 - j)
            temp = 0
            if lis[i] + 2 - j in index:
                temp = comb(index[lis[i] + 2 - j] - i, 2)
            if temp > 0:
                # print(index[lis[i] + 2 -j], temp, i)
                count += temp
                break
    print(int(count))
