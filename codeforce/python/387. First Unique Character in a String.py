class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        lis = {}
        for i in range(len(s)):
            if s[i] not in dic and s[i] not in lis:
                dic[s[i]] = i
                lis[s[i]] = 1
            elif s[i] in dic:
                dic.pop(s[i])
        _min = 2**31
        for i in dic:
            if dic[i] < _min:
                _min = dic[i]
        if _min == 2**31:
            return -1
        return _min
            