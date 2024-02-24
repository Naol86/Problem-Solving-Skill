from collections import defaultdict
for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    if x < 3:
        print(0)
        continue
    freq = defaultdict(int)
    _max = -float('inf')
    for i in lis:
        freq[i] += 1
        _max = max(_max, i)
    count = 0
    left = 0
    right = left + 1
    _sum = lis[0]
    while left < x - 1:
        if right == x or _sum > _max:
            left += 1
            right = left + 1
            _sum = lis[left]
            continue
        _sum += lis[right]
        if _sum in freq:
            count += freq[_sum]
            freq.pop(_sum)
        right += 1
    print(count)