class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lis1 = nums.copy()
        lis2 = nums.copy()
        for i in range(1,len(nums)):
            lis1[i] = lis1[i-1] + lis1[i]
            lis2[-i-1] = lis2[-i-1] + lis2[-i]
        for i in range(len(nums)):
            if lis1[i] == lis2[i]:
                return i
        return -1