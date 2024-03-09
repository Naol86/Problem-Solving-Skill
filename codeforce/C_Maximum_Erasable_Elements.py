import sys 
input = sys.stdin.readline

x = int(input())
nums = [int(i) for i in input().split()]
nums.append(2000)

cons = []
start = 0
for i in range(1, x + 1):
    if nums[i] == nums[i - 1] + 1:
        continue
    else:
        if i - start > 1:
            cons.append(nums[start:i])
        start = i

count = 0
for num in cons:
    if num[0] == 1 and num[-1] == 1000:
        count = max(count, len(num) - 2)
    elif num[0] == 1:
        count = max(count, len(num) - 1)
    elif num[-1] == 1000:
        count = max(count, len(num) - 1)
    else:
        count = max(count, len(num) - 2)
print(count)