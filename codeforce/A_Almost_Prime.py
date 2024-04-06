import math


x = int(input())

nums = [True] * (math.ceil(x/2) + 1)

nums[0] = False
nums[1] = False
i = 2
while i < len(nums):
    if nums[i]:
        for j in range(i*i, len(nums), i):
            nums[j] = False
    i += 1

nums = [i for i in range(len(nums)) if nums[i]]
count = 0
# print(len(nums))
i = 6
while i <= x:
    temp = 0
    ind = 0
    while ind < len(nums):
        if i % nums[ind] == 0:
            temp += 1
        ind += 1
        if temp > 2:
            break
    if temp == 2:
        count += 1
    i += 1
print(count)