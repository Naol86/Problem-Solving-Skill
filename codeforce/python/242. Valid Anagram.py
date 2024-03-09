class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        dic2 = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] +=1
        for i in range(len(t)):
            if t[i] not in dic2:
                dic2[t[i]] = 1
            else:
                dic2[t[i]] +=1
        if dic == dic2:
            return True
        else:
            return False