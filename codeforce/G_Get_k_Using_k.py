import sys 
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = [int(i) for i in input().split()]
    nums = [int(i) for i in input().split()]
    _sum = 0
    for num in nums:
        _sum += num
    if _sum % y == 0:
        print("YES")
    else:
        print("NO")