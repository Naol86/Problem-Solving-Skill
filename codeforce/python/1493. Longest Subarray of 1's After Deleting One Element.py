class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        a = 0
        b = 0
        dele = 0
        while b < len(nums):
            if nums[b] == 0 and dele < 1:
                b+=1
                dele +=1
            elif nums[b] == 0 and dele > 0:
                if nums[a] == 1:
                    dele += 1
                a+=1
                b+=1
            elif nums[b] == 1 and dele <= 1:
                b+=1
            else:
                if nums[a] == 0:
                    dele -= 1
                a+=1
                b+=1
        return b - a - 1
