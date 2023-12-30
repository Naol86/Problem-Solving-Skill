from collections import Counter
for _ in range(int(input())):
    x = int(input())
    s = input()
    dic  = Counter(s)
    lis = list(dic.values())
    _max = max(lis)
    if _max > (x - _max):
        ans = _max - (x - _max)
        print(ans)
    else:
        print(x%2)
