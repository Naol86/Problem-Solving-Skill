from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            valid = True
            for j in range(1, len(strs)):
                if (i < len(strs[j]) and strs[0][i] != strs[j][i]) or i >= len(strs[j]):
                    valid = False
                    break
            if valid:
                ans = str(strs[0][:i+1])
            else:
                break
        return ans



