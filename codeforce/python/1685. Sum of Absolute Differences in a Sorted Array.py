class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        _sum = sum(nums)
        left = 0
        right = _sum
        for i in range(len(nums)):
            n = nums[i]
            right -= n
            temp = n * i - left + right - n * (len(nums) - i - 1)
            ans.append(temp)
            left+=n
        return ans