from collections import Counter

for _ in range(int(input())):
    lis = Counter()
    x = int(input())
    for i in range(x):
        temp = input()
        lis += Counter(temp)
    for key, value in lis.items():
        if value % x != 0:
            print("NO")
            break
    else:
        print("YES")