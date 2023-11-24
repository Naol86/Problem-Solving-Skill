class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Max = sum(nums[:k])
        temp = Max
        a = 0
        b = k
        while b < len(nums):
            temp = temp - nums[a] + nums[b]
            if temp > Max:
                Max = temp
            a+=1
            b+=1
        return Max/k
