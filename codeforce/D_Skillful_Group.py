from collections import Counter, defaultdict


x = int(input())
lis = [int(i) for i in input().split()]

freq = Counter(lis)
comp = defaultdict(int)

for key, value in freq.items():
    if value > 1:
        comp[key] += value - 1

def check(window, comp):
    for key, value in comp.items():
        if key not in window:
            return False
        if value > window[key]:
            return False
    return True


if len(comp) == 0:
    print(0)
else:
    _min = float("inf")
    window = defaultdict(int)
    left = right = 0
    while right < x:
        if check(window, comp):
            _min = min(_min, right - left)
            window[lis[left]] -= 1
            left += 1
        else:
            window[lis[right]] += 1
            right += 1
    print(_min)