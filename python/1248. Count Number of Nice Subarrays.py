from typing import List

class Solution:
    def odd(self, lis):
        count = 0
        for i in lis:
            if i%2 !=0:
                count +=1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        a = 0
        b = k
        count = self.odd(nums[:k])
        check = True
        while a < len(nums) - k and check:
            if 