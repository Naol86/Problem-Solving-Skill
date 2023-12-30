from collections import Counter, defaultdict
for _ in range(int(input())):
    x = int(input())
    lis = [int(i) for i in input().split()]
    count = Counter(lis)

    set_count = set(count.values())
    set_count = list(set_count)
    freq = defaultdict(int)

    for key, val in count.items():
        freq[val] += 1
    _max = 10 ** 6 + 1
    # print(freq)

    for i in set_count:
        _sum = 0
        for j in set_count:
            # print(i,j)
            if i <= j:
                # print(freq[j] * (j - i))
                _sum += freq[j] * (j - i)
            else:
                # print(freq[j] * (j))
                _sum += freq[j] * j
        # print(_sum)
        _max = min(_max, _sum)
    print(_max)