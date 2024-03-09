class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        lis=[]
        temp=[]
        for i in s:
            if i not in temp:
                temp+=i
            else:
                lis+=[len(temp)]
                temp = temp[temp.index(i)+1:]
                temp+=[i]
        lis+=[len(temp)]
        lis.sort()
        return lis[-1]