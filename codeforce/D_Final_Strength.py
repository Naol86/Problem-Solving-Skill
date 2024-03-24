import bisect
from copy import deepcopy

inputs = []
for _ in range(int(input())):
    x = int(input())
    nums = [int(i) for i in input().split()]
    inputs.append([x, nums])

for x, nums in inputs:
    for i in range(2 ** x):
        nums[i] = [nums[i], i]
    ans = nums
    # print(nums)
    def merge(lis1, lis2):
        ans = []
        left = 0
        right = 0
        while left < len(lis1) and right < len(lis2):
            if lis1[left] <= lis2[right]:
                ans.append(lis1[left])
                left += 1
            else:
                ans.append(lis2[right])
                right += 1
        ans.extend(lis1[left:])
        ans.extend(lis2[right:])
        return ans
    
    def divide(left, right):
        if left == right:
            return [nums[left]]
        mid = left + (right - left) // 2
        left_half = divide(left, mid)
        right_half = divide(mid + 1, right)
        # print(left_half, right_half)
        temp = deepcopy(left_half)
        for i in left_half:
            pos = bisect.bisect_left(right_half,[i[0], float('-inf')])
            ans[i[1]][0] += pos
        for i in right_half:
            pos = bisect.bisect_left(temp,[i[0], float('-inf')])
            # print(i, pos, left_half)
            ans[i[1]][0] += pos
        # for i in left_half:
        #     i[0] = ans[i[1]][0]
        # for i in right_half:
        #     i[0] = ans[i[1]][0]
        # print(nums)
        return merge(left_half, right_half)
    divide(0, 2 ** x - 1)
    ans = [i for i,j in ans]
    print(*ans)