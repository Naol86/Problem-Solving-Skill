import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    lis = input()
    _sum = 0
    ans = []
    for i in range(x):
        if lis[i] == 'L':
            _sum += i
        else:
            _sum += x - i - 1
    # print(_sum)
    left = 0
    right = x - 1
    for __ in range(x):
        if left > x//2 and right < x//2:
            break
        while left < x // 2 and lis[left] != 'L':
            left += 1
        while right >= x // 2 and lis[right] != 'R':
            right -= 1
        if left > right:
            break
        # print(left, right)
        l = x - left - 1 - left if left < x // 2 else 0
        r = right - (x - right - 1) if right >= (x//2) else 0
        # print(l,r,'------')
        if l > r:
            _sum += l
            left += 1
        else:
            _sum += r
            right -= 1
        ans.append(_sum)
    leng = len(ans)
    last = _sum if ans == [] else ans[-1]
    while leng < x:
        ans.append(last)
        leng += 1
    print(*ans)
    # print('--------------------')
    print(225%26)
[['5', '3', 4, 6, '7', 8, 9, 1, 2],
 ['6', 7, 2, '1', '9', '5', 3, 4, 8],
 [1, '9', '8', 3, 4, 2, 5, '6', 7],
 ['8', 5, 9, 7, '6', 1, 4, 2, '3'],
 ['4', 2, 6, '8', 5, '3', 7, 9, '1'],
 ['7', 1, 3, 9, '2', 4, 8, 5, '6'],
 [9, '6', 1, 5, 3, 7, '2', '8', 4],
 [2, 8, 7, '4', '1', '9', 6, 3, '5'], 
 ['.', '.', '.', '.', '8', '.', '.', '7', '9']]