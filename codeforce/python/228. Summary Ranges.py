from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return []
        temp = f"{nums[0]}"
        for i in range(1, len(nums)):
            print(nums[i], temp)
            if nums[i-1]+1 != nums[i]:
                if temp == f"{nums[i-1]}":
                    ans += [temp]
                    temp = f"{nums[i]}"
                else:
                    temp = temp + f"->{nums[i-1]}"
                    ans += [temp]
                    temp = f"{nums[i]}"
        if len(nums) > 0 and temp != f"{nums[-1]}":
            temp = temp + f"->{nums[-1]}"
        ans += [temp]
        return ans

