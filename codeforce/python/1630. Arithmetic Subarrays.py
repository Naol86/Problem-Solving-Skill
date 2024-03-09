class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(r)):
            temp = nums[l[i]:r[i]+1]
            if len(temp) < 2:
                ans.append(True)
                continue
            temp.sort()
            diff = temp[0] - temp[1]
            for j in range(1,len(temp)):
                if temp[j-1] - temp[j] != diff:
                    ans.append(False)
                    break
            else:
                ans.append(True)
        return ans