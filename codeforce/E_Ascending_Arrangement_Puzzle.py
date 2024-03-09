import sys 
input = sys.stdin.readline

x = int(input())
nums = [int(i) for i in input().split()]
s = input()
temp = sorted(nums)

left = x
right = 0

for i in range(x):
    if nums[i] != temp[i]:
        left = min(left, i)
        right = max(right, i)

for i in range(left, right):
    if s[i] == '0':
        print('NO')
        break
else:
    print('YES')