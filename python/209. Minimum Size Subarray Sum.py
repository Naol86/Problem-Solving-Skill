class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        _min = 10 ** 5 + 10
        nums = [0] + nums
        for i in range(1,len(nums)):
            nums[i] = nums[i] + nums[i-1]
        a=0
        b=0
        while b < len(nums):
            if nums[b] - nums[a] >= target:
                if _min > b-a:
                    _min = b - a
                    if _min == 1:
                        return _min
                a+=1
            else:
                b+=1
        if _min == 10**5 + 10:
            return 0
        return _min
