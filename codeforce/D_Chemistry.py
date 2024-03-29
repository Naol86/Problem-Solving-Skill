from collections import Counter


for _ in range(int(input())):
    n, k = [int(i) for i in input().split()]
    s = input()
    count = Counter(s)
    odd = 0
    for i in count.values():
        if i % 2:
            odd += 1
    if odd > k + 1:
        print("NO")
        continue
    print("YES")