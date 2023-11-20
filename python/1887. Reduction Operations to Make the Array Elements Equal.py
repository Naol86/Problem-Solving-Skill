from typing import List
import numpy as np

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        temp = np.array([])
        _min = nums[0]
        for i in nums:
            if i < _min:
                _min = i
            if i not in temp:
                # temp = temp
                temp = np.append(temp, i)
        temp.sort()
        dic = {}
        for i in range(len(temp)):
            dic[temp[i]] = i
        ans = 0
        for i in nums:
            ans += dic[i]

        return ans

ob = Solution()
ob.reductionOperations([1,2,3])