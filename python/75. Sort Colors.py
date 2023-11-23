class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            t = i
            for j in range(i - 1,-1,-1):
                if nums[t] < nums[j]:
                    temp = nums[t]
                    nums[t] = nums[j]
                    nums[j] = temp
                    t-=1
                else:
                    break