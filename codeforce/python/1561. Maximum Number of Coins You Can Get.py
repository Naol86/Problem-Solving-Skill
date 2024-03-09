class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        a = 0
        b = len(piles) - 2
        while b > a:
            ans += piles[b]
            a+=1
            b-=2
        return ans
