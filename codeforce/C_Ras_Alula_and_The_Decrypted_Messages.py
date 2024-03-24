from collections import defaultdict


for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    word1 = input()
    word2 = input()
    
    total = 0
    for i in word2:
        total += ord(i)
    prefix = [0]
    _dict = defaultdict(int)
    _dict[0] = -1
    
    _sum = 0
    for i in range(len(word1)):
        _sum += ord(word1[i])
        if _sum - total in _dict and (i - _dict[_sum - total]) == len(word2):
            print("YES")
            break
        _dict[_sum] += i
    else:
        print("NO")