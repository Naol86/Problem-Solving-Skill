import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    lis = input()
    lis = [int(i) for i in lis[:-1]]
    # print(lis)
    
    prev = 0
    ans = 0
    _sum = 0
    for i in range(1, x + 1):
        _sum += lis[i - 1]
        if _sum == i or lis[i - 1] == 1:
            prev += 1
            ans += prev
        else:
            prev = 0
    print(ans)