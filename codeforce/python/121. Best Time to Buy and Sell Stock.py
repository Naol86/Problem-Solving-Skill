
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max = Min = prices[0]
        ans=[]
        for i in range(1,len(prices)):
            print(ans)
            if prices[i]<Min:
                ans+=[Max-Min]
                Min=prices[i]
                Max=prices[i]
            elif Max<prices[i]:
                Max=prices[i]
        if (Max-Min) not in ans:
            ans+=[Max-Min]
        ans.sort()
        return ans[-1]

ob = Solution()
ob.maxProfit([7,1,5,3,6,4])