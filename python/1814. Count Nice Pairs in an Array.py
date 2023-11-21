class Solution:
    def rev(self, num):
        a = str(num)
        a = a[::-1]
        return int(a)
    def countNicePairs(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        ans = 0
        dic = {}
        for i in nums:
            if i - Solution.rev(self, i) in dic:
                ans += dic[i - Solution.rev(self, i)]
                dic[i - Solution.rev(self, i)] += 1
            else:
                dic[i - Solution.rev(self, i)] = 1
        return ans % (10 ** 9 +7)