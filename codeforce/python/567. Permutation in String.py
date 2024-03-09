class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        lis = {}
        temp = {}
        for i in range(len(s1)):
            if s1[i] in lis:
                lis[s1[i]] += 1
            else:
                temp[s1[i]] = 0
                lis[s1[i]] = 1
        for i in range(len(s1)):
            if s2[i] in temp:
                temp[s2[i]] +=1
        if lis == temp:
            return True
        a = 0
        b = len(s1)
        while b < len(s2):
            if s2[b] in temp:
                temp[s2[b]] +=1
            if s2[a] in temp:
                temp[s2[a]] -=1
            if temp == lis:
                return True
            b+=1
            a+=1
        return False