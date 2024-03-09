import sys 
input = sys.stdin.readline

x = int(input())
nums = [int(i) for i in input().split()]

left = 0
right = 0
for num in nums:
    if num < 0:
        right += num
    else:
        left += num
print(left - right)