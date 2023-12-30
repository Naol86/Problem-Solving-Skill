from collections import defaultdict
for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    dic = defaultdict(int)
    index = defaultdict(int)
    for i in range(x):
        dic[lis[i]] += 1
        index[lis[i]] += i
    for i in dic:
        if dic[i] == 1:
            print(index[i]+1)
            break