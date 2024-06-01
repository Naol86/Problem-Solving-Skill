from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices.copy()
        _max = prices.copy()
        for i in range(1, len(prices)):
            _min[i] = min(_min[i-1], _min[i])
        for i in range(len(prices) - 2, -1, -1):
            _max[i] = max(_max[i], _max[-1-1])
        # print(_min)
        # print(_max)
        _min[0] = 0
        _max[-1] = 0
        for i in range(1, len(prices)):
            _min[i] = max(prices[i] - _min[i], _min[i-1])
        for i in range(len(prices) - 2, -1, -1):
            _max[i] = max(_max[i] - prices[i], _max[i + 1])

        print(_min)
        print(_max)
        ans = _max[0]
        for i in range(len(prices) - 1):
            if ans < _min[i] + _max[i+1]:
                print(i, _min[i], _max[i])
            ans = max(ans, _min[i] + _max[i+1])
        return ans
ob = Solution()
nums = input()[1:-1]
nums = [int(i) for i in nums.split(',')]
ob.maxProfit(nums)