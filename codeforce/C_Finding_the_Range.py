from collections import defaultdict

row = []
for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    lis = [int(i) for i in input().split()]
    lis.sort()
    temp_set = set()
    temp_lis = []
    count = defaultdict(int)
    for i in lis:
        count[i] += 1
        if count[i] >= y and i not in temp_set:
            temp_lis.append(i)
            temp_set.add(i)
    row.append(temp_lis)

for temp_lis in row:

    if len(temp_lis) == 0:
        print(-1)
        continue
    temp_lis.sort()
    temp_lis.append(temp_lis[-1] + 2)
    diff = 0
    _max = _min = prev = current = temp_lis[0]
    for i in temp_lis[1:]:
        if i != current + 1:
            if diff < (current - prev):
                _min = prev
                _max = current
                diff = _max - _min
            prev = i
        current = i
    print(_min, _max)