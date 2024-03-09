class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        _min = nums[0]
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
            if nums[i] < _min:
                _min = nums[i]
        ans = - (_min - 1)
        if ans < 1:
            return 1
        return ans
